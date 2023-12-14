# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:42:22 2023

@author: jmeluso
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns
from string import ascii_lowercase

import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()    
    
def plot_compensation(baseVar='credit_freqFromProjects', save=True):
    
    # Define numeric variables group 01
    numVars = [
        'credit_freqFromProjects',
        'credit_freqForTasks',
        'satis_taskFreq',
        'satis_medium'
    ]
    
    # Total number of survey responses
    total = 142
    
    # Load question groups
    question2group = uv.get_question_groups()
    
    # Load split data for groups of variables
    dtype2layout2df = io.load_survey_dict()
    df = dtype2layout2df['numeric']['split']
    
    # Load unified data for means of variables and replace 6's with nans
    stats = dtype2layout2df['numeric']['unified'].replace(6,np.nan).describe()
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Create a figure with 4 axes
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=fs.fig_size(1, 0.4),
                            layout='tight', sharex=True, sharey='row')
    
    # Generate color palette
    colors = sns.color_palette('mako_r', n_colors=5).as_hex()
    colors.append('#666666')
    
    # Create the base variables for comparison
    dfBase = df.loc[:,question2group[baseVar]]
    
    # Create a dictionary for storing percent and sum info
    summary = {'percents': {}, 'sums': {}}
    
    # Cycle through axes (flat) and populate them for each variable
    for var, ax, letter in zip(numVars, axs.flat, ascii_lowercase):
        
        # Get the variable's group
        group = question2group[var]
        
        # Slice down data to variable subset
        subset = df.loc[:,group]
        
        sums = []
        percents = []
        
        # Loop through the base variables and colors
        for bv in dfBase.columns:
            
            # Count the overlap between the base variables and this var
            data = subset.multiply(dfBase.loc[:,bv], axis=0)
            
            # Get the count and fraction of respondents who gave each response
            sums.append(data.sum())
            percents.append(data.sum()/total)
            
        # Turn sums and percents into dataframes
        sums = pd.concat(sums, axis=1, keys=subset.columns)
        percents = pd.concat(percents, axis=1, keys=subset.columns)
        
        # Sum and append eahch to the summary dictionary
        summary['sums'][var] = sums.sum(axis=1)
        summary['percents'][var] = percents.sum(axis=1)
        
        # Plot the mean and standard deviation
        statsColor = '#222222'
        ax.errorbar(x=0.375, y=stats.loc['mean',var]-1, capsize=3, fmt='.',
                    yerr=stats.loc['std',var],ecolor=statsColor, ms=8,
                    markerfacecolor='#FFFFFF', markeredgecolor=statsColor)
            
        # Plot the percents on the axes
        percents.plot(kind='barh', ax=ax, width=0.8, color=colors,
                      stacked=True, legend=False)
        
        # Add title
        ax.set_title(f'({letter}) {optionDefs[var]}')
        
        # Update labels
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
        ax.set_yticklabels([optionDefs[index] for index in percents.index])
        
        # Remove borders
        fs.set_border(ax, left=True)
        
        # Add grid
        ax.grid(True)
        ax.set_axisbelow(True)
        
        # Get the handles and labels if it's the base variable
        if var == baseVar: handles, labels = ax.get_legend_handles_labels()
    
    # Add legend
    title = 'Colors based on (a),\nproject credit frequency'
    labels = ['1 - None of them', '2 - Few of them', '3 - Some of them',
              '4 - Most of them', '5 - All of them', "I'm not sure"]
    fig.legend(handles, labels, loc='center right', title=title,
               title_fontsize=10, alignment='center', bbox_to_anchor=(0, 0.5))
    
    # Save the plot!
    if save: fs.save_publication_fig('compensation', bbox_inches='tight')
    
    return summary, stats
        
    
if __name__ == '__main__':
    summary, stats = plot_compensation()
