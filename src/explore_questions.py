# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:18:20 2023

@author: jmeluso
"""

import itertools as it
import matplotlib.pyplot as plt
from matplotlib.colors import SymLogNorm
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns

import util.fig_settings as fs
import util.io as io
import util.variables as uv

def plot_barh(question,dtype='numeric',layout='split',total=142,sort=False):
    
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

def plot_joint_multiselects(question1, question2):
    
    # Set a couple variables
    dtype = 'numeric'
    layout = 'split'
    
    # Load question group
    question2group = uv.get_question_groups()
    group1 = question2group[question1]
    group2 = question2group[question2]
    
    # Load data for groups of variables
    dtype2layout2df = io.load_survey_dict()
    df = dtype2layout2df[dtype][layout].loc[:,group1 + group2]
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Create a dataframe of count coincidences for both groups
    df_counts = pd.DataFrame(index=group1, columns=group2)
    
    # Count the number of times elements of group1 & group2 coincide
    for g1, g2 in it.product(group1, group2):
        groups_coincide = (df.loc[:,g1] == 1) & (df.loc[:,g2] == 1)
        df_counts.loc[g1,g2] = groups_coincide.sum()
    
    # Sort the counts df by the sum of the rows and the columns
    df_counts = df_counts.loc[
        df_counts.sum(axis=1).sort_values(ascending=False).index,
        df_counts.sum(axis=0).sort_values(ascending=False).index,
        ]
    
    # Coerce columns to numeric
    for col in df_counts:
        df_counts[col] =  pd.to_numeric(df_counts[col], errors='coerce')
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Update index and column names
    df_counts.index = [optionDefs[ii] for ii in df_counts.index]
    df_counts.columns = [optionDefs[cc] for cc in df_counts.columns]
    
    # Plot the data as a heatmap
    fig = plt.figure(dpi=1200)
    ax = fig.gca()
    sns.heatmap(
        df_counts,
        annot=True,
        norm=SymLogNorm(10),
        cbar_kws={'ticks':mtick.MaxNLocator(7), 'format':'%.f'},
        ax=ax,
        )
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right',
                       rotation_mode="anchor")

def plot_project_artifact():
    '''Question 3: The following categories describe things that projects
    either create or work on. Which categories apply to the projects you 
    worked on? Select all that apply.'''
    plot_barh(question='project_artifact', sort=True)

def plot_project_useCase():
    '''Question 4: Projects create for different use cases. Which cases apply
    to the projects you worked on? Select all that apply.'''
    plot_barh(question='project_useCase', sort=True)

def plot_credit_freqFromProjects():
    '''Question 7: In the past two years, from how many projects did you
    receive credit for your tasks?'''
    plot_barh(question='credit_freqFromProjects')
    
def plot_credit_freqForTasks():
    '''Question 8: In the past two years, for how many of your tasks did you
    receive credit?'''
    plot_barh(question='credit_freqForTasks')
    
def plot_credit_medium():
    '''Question 9: Projects give people credit for tasks through different
    mediums. Through what mediums did you receive credit? Select all
    that apply.'''
    plot_barh(question='credit_medium', sort=True)

def plot_satis_medium():
    '''Question 10: How satisfied are you with the mediums through which you
    received credit?'''
    plot_barh(question='satis_medium')

def plot_freq_seenBy2():
    '''Question 11: How often did 2 or more people know that you performed
    those tasks?'''
    plot_barh(question='freq_seenBy2')

def plot_freq_seenBy1():
    '''Question 12: How often did 1 other person know that you performed
    those tasks?'''
    plot_barh(question='freq_seenBy1')
    
def plot_freq_seenBy0():
    '''Question 13: How often did nobody else know that you performed
    those tasks?'''
    plot_barh(question='freq_seenBy0')
    
def plot_satis_taskFreq():
    '''Question 14: How satisfied are you with how many of your tasks
    received credit?'''
    plot_barh(question='satis_taskFreq')

def plot_credit_importance():
    '''How important is it to you to receive credit for the tasks you do?'''
    plot_barh(question='credit_importance')
    

if __name__ == '__main__':
    
    # Question 3 
    plot_project_artifact()
    
    # Question 4
    plot_project_useCase()
    
    # Q3 & Q4 Joint
    # plot_joint_multiselects('project_artifact', 'project_useCase')
    
    # Question 7
    plot_credit_freqFromProjects()

    # Question 8
    plot_credit_freqForTasks()

    # Question 9
    plot_credit_medium()

    # Question 10
    plot_satis_medium()

    # Question 11
    plot_freq_seenBy2()

    # Question 12
    plot_freq_seenBy1()

    # Question 13
    plot_freq_seenBy0()

    # Question 14
    plot_satis_taskFreq()

    # Question 15
    plot_credit_importance()

    
