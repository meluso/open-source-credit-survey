# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:43:32 2023

@author: jmeluso
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
from numpy import nan
import pandas as pd
import seaborn as sns
from string import ascii_lowercase as asciiLower

import util.analysis as ua
import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()

    
def plot_numeric_plt1(save=True):
    
    # Set questions to slice down to, and values for those vars to replace
    numVars = {
        'freq_seenBy2': 16,
        'freq_seenBy1': 0,
        'freq_seenBy0': 0,
        }
    
    # Total number of survey responses
    total = 142
    
    # Load question groups
    question2group = uv.get_question_groups()
    
    # Load split data for groups of variables
    dtype2layout2df = io.load_survey_dict()
    
    # Load unified data for means of variables and replace 6's with nans
    stats = dtype2layout2df['numeric']['unified'].replace(6,np.nan).describe()
    
    # Build the dataframe with the text order column on the end
    df = pd.concat([
        dtype2layout2df['numeric']['split'],
        dtype2layout2df['text']['unified']['order']],
        axis=1
        )
    
    # Create statistics dataframe
    statsDf = dtype2layout2df['numeric']['unified']
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Create a figure with 4 axes
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=fs.fig_size(1, 0.25),
                            layout='tight', sharey=True)
    
    # Generate color palette
    colors = sns.color_palette('mako', n_colors=2).as_hex()
    
    # Create a list of the order options
    orderOpts = pd.Series(df.order.dropna().unique())
    
    # Cycle through axes (flat) and populate them for each variable
    for var, ax, letter in zip(numVars, axs.flat, asciiLower):
        
        # Get the variable's group
        group = question2group[var]
        
        # Create stats dataframe, and subtract offsets as needed
        statsDf = dtype2layout2df['numeric']['unified'][var].replace(6,np.nan)
        statsDf = statsDf - numVars[var]
        
        # Create empty list of percents
        percents = []
        
        # Loop through the variables and colors
        for ii, (oo, color) in enumerate(zip(orderOpts, colors)):
            
            # Slice down data to variable subset
            data = df.loc[df['order'] == oo,group]
            
            # Get the fraction of respondents who gave each response
            percents.append(data.sum()/total)
            
            # Calculate stats for current order option
            stats = statsDf[df['order'] == oo].describe()
            
            # Calculate confidence interval
            lower, upper = ua.conf_int_mean(statsDf[df['order']==oo].dropna())
            lowerBound = stats['mean']-lower
            upperBound = upper-stats['mean']
            confInt = np.array(lowerBound,upperBound)
            
            # Plot the mean and standard deviation
            ax.errorbar(
                x = 0.38 + ii*0.04,
                y = stats['mean'] - 1,
                yerr=confInt,
                capsize=3,
                fmt='.',
                markersize=8,
                ecolor=color,
                markerfacecolor='#FFFFFF',
                markeredgecolor=color
                )
                
        # Turn percents into a dataframe
        percents = pd.concat(percents, axis=1, keys=oo)
        
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
        
        # Get the handles and labels
        handles, __ = ax.get_legend_handles_labels()
        labels = orderOpts
        
    # Create legend
    title = 'Question presentation order'
    fig.legend(handles, labels, loc='center right', bbox_to_anchor=(0, 0.5),
               title=title, title_fontsize=8)
    
    # Save the plot!
    if save: fs.save_publication_fig('numeric_01', bbox_inches='tight')
    
    pass

def plot_numeric_plt2(save=True):
    
    # Set questions to slice down to, and values for those vars to replace
    numVars = {
        'freq_seenBy2': 16,
        'freq_seenBy1': 0,
        'freq_seenBy0': 0,
        # 'credit_importance': 27,
        }
    
    # Total number of survey responses
    total = 142
    
    # Load question groups
    question2group = uv.get_question_groups()
    
    # Load split data for groups of variables
    dtype2layout2df = io.load_survey_dict()
    
    # Load unified data for means of variables and replace 6's with nans
    stats = dtype2layout2df['numeric']['unified'].replace(6,np.nan).describe()
    
    # Build the dataframe with the text order column on the end
    df = pd.concat([
        dtype2layout2df['numeric']['split'],
        dtype2layout2df['text']['unified']['order']],
        axis=1
        )
    
    # Create statistics dataframe
    statsDf = dtype2layout2df['numeric']['unified']
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Create a figure with 4 axes
    fig, axs = plt.subplots(nrows=1, ncols=len(numVars),
                            figsize=fs.fig_size(1, 0.25),
                            layout='tight', sharey=True)
    
    # Generate color palette
    colors = sns.color_palette('mako', n_colors=2).as_hex()
    
    # Create a list of the order options
    orderOpts = pd.Series(df.order.dropna().unique())
    
    # Cycle through axes (flat) and populate them for each variable
    for ii, (var, ax, letter) in enumerate(zip(numVars, axs.flat, asciiLower)):
        
        # Get the variable's group
        group = question2group[var]
        
        # Create stats dataframe, and subtract offsets as needed
        statsDf = dtype2layout2df['numeric']['unified'][var].replace(6,np.nan)
        statsDf = statsDf - numVars[var]
        
        # Create empty list of percents
        percents = []
        
        # Loop through the variables and colors
        for jj, (oo, color) in enumerate(zip(orderOpts, colors)):
            
            # Slice down data to variable subset
            data = df.loc[df['order'] == oo,group]
            
            # Get the fraction of respondents who gave each response
            percents.append(data.sum()/total)
            
            # Calculate stats for current order option
            stats = statsDf[df['order'] == oo].describe()
            
            # Calculate confidence interval
            lower, upper = ua.conf_int_mean(statsDf[df['order']==oo].dropna())
            lowerBound = stats['mean']-lower
            upperBound = upper-stats['mean']
            confInt = np.array(lowerBound,upperBound)
            
            # Plot the mean and standard deviation
            ax.errorbar(
                x = 0.37 + jj*0.02,
                y = stats['mean'] - 1,
                yerr=confInt,
                capsize=5,
                fmt='.',
                # markersize=8,
                ecolor=color,
                markerfacecolor=color,
                markeredgecolor=color
                )
                
        # Turn percents into a dataframe
        percents = pd.concat(percents, axis=1, keys=oo)
        
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
        
        # Get the handles and labels
        handles, __ = ax.get_legend_handles_labels()
        labels = orderOpts
        
    # Create legend
    title = 'Question presentation order'
    fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0),
               title=title, title_fontsize=8, ncols=2)
    
    # Save the plot!
    if save: fs.save_publication_fig('numeric_01', bbox_inches='tight')
    
    pass
    
if __name__ == '__main__':
    # plot_numeric_plt1(False)
    plot_numeric_plt2(False)
