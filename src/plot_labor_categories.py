# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:43:15 2023

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

def plot_categorical(save=True, sort=True):
    
    # Set dtype, layout, and total
    dtype = 'numeric'
    layout = 'split'
    total = 142
    
    # Questions to plot
    questions = ['project_artifact','project_useCase']
    
    # Load question group
    question2group = uv.get_question_groups()
    
    # Load data for group of variables
    dtype2layout2df = io.load_survey_dict()
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Plot the counts
    fig, axs = plt.subplots(nrows=1, ncols=len(questions),
                            figsize=fs.fig_size(1, 0.2), layout='constrained')
    
    # Generate color palette and select the color for all bars
    colors = sns.color_palette('mako_r', n_colors=5).as_hex()
    colors = (colors[1],colors[3])
    
    # Cycle through questions
    for qq, ax, letter, color \
        in zip(questions, axs.flat, ascii_lowercase, colors):
        
        # Load the variables just for this question
        group = question2group[qq]
        
        # Slice the data down to the correct subset
        df = dtype2layout2df[dtype][layout].loc[:,group]
        
        # Count fraction of people who responded with each item, and sort them
        counts = df.sum()
        if sort: counts = counts.sort_values()
        percents = counts/total
    
        # Plot the data as bars on the appropriate ax
        bars = ax.barh(
            y=range(len(percents)),
            width=percents,
            height=0.8,
            color=color,
            tick_label=percents.index
            )
        
        # Define label groups
        cutoff = 0.10
        labelGroups = {
            'large': (
                -11,
                [f'{100*p:.0f}%' if p >= cutoff else '' for p in percents]
                ),
            'small': (
                -8,
                [f'{100*p:.0f}%' if p < cutoff else '' for p in percents]
                )
            }
        
        # Iterate through label groups to create labels
        for padding, labels in labelGroups.values():
            labels = ax.bar_label(
                bars,
                labels=labels,
                color='#FFFFFF',
                size=6,
                padding=padding,
                fontweight='bold'
                )
    
        # Add title
        ax.set_title(f'({letter}) {optionDefs[qq]}')
        
        # Update labels
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
        ax.set_yticklabels([optionDefs[index] for index in counts.index])
        
        # Remove borders
        fs.set_border(ax, left=True)
        
        # Add grid
        ax.grid(True)
        ax.set_axisbelow(True)
        
    # Save the plot
    if save: fs.save_publication_fig('labor_categories', bbox_inches='tight')

if __name__ == '__main__':
    plot_categorical(save=True)
