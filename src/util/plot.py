# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:07:13 2023

@author: jmeluso
"""    
    
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

import util.fig_settings as fs
import util.io as io
import util.variables as uv

def arrow(ax, xyfrom, xyto, text=''):
    an = ax.annotate(text=text, xy=xyto, xytext=xyfrom, annotation_clip=False,
        arrowprops=dict(arrowstyle='->',fc='#AAAAAA',ec='#AAAAAA'),
        xycoords='axes fraction')
    return an

def plot_multi(question,dtype='numeric',layout='split',total=142,sort=False):
    
    # Load question group
    question2group = uv.get_question_groups()
    group = question2group[question]
    
    # Load data for group of variables
    dtype2layout2df = io.load_survey_dict()
    df = dtype2layout2df[dtype][layout].loc[:,group]
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Count fraction of people who responded with each item, and sort them
    counts = df.sum()
    if sort: counts = counts.sort_values()
    percents = counts/total
    
    # Plot the counts
    fig = plt.figure(dpi=300)
    ax = fig.gca()
    percents.plot(kind='barh', ax=ax)
    
    # Add title
    ax.set_title(f'Variable: {question}')
    
    # Update labels
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.set_yticklabels([optionDefs[index] for index in counts.index])
    
    # Remove borders
    fs.set_border(ax, left=True)
    
    # Add grid
    ax.grid(True)
    ax.set_axisbelow(True)

def plot_multi(questionX, questionY):
    
    # Load dataframe
    df = io.load_survey_df()
    
    # Load question groups
    question2group = uv.get_question_groups()
    groupX = question2group[questionX]
    groupY = question2group[questionY]
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Slice down to just those two questions
    df = df.loc[:, ([questionX, questionY], 'numeric', 'unified')]
    
    # Remove any 6's which represent I don't know's
    df = df.replace(6,np.nan)
    
    # Plot the counts
    fig, ax = plt.subplots(dpi=300)
    
    # Add title
    ax.set_title(f'{questionX} vs. {questionY}')
    
    # Add grid
    ax.grid(True)
    
# def plot_category_means(catgroup, question, sort=False, total=142):
    
#     # Load question group
#     catgroup2group = uv.get_question_groups()
#     group = catgroup2group[catgroup]
    
#     # Load data for group of variables
#     dtype2layout2df = io.load_survey_dict()
#     df = dtype2layout2df[dtype][layout].loc[:,group]
    
#     # Load option definitions
#     optionDefs = uv.get_option_definitions()
    
#     # Count fraction of people who responded with each item, and sort them
#     counts = df.sum()
#     if sort: counts = counts.sort_values()
#     percents = counts/total
    
#     # Plot the counts
#     fig = plt.figure(dpi=300)
#     ax = fig.gca()
#     percents.plot(kind='barh', ax=ax)
    
#     # Add title
#     ax.set_title(f'Variable: {question}')
    
#     # Update labels
#     ax.xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
#     ax.set_yticklabels([optionDefs[index] for index in counts.index])
    
#     # Remove borders
#     fs.set_border(ax, left=True)
    
#     # Add grid
#     ax.grid(True)
#     ax.set_axisbelow(True)
