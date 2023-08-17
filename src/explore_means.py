# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:52:26 2023

@author: jmeluso
"""

import matplotlib.pyplot as plt
from numpy import nan
import pandas as pd
import seaborn as sns

import util.io as io
import util.variables as uv

def explore_means():
    
    # Load survey data
    df = io.load_survey_df()
    
    # Load numeric variables
    numVars = uv.get_variables_numeric()
    
    # Slice down to just numeric and unified data
    df = df.xs(('numeric', 'unified'), level=(1,2), axis=1)
    
    # Now slice to just numeric variables
    df = df.loc[:,numVars]
    
    # Replace I'm not sure's with nans
    df = df.replace(6,nan)
    
    # Adjust value range for freq_seenBy2 (subtract 16)
    df.freq_seenBy2 = df.freq_seenBy2 - 16
    
    # Adjust value range for credit_importance (subtract 27)
    df.credit_importance = df.credit_importance - 27
    
    # Melt from wide to long
    df = pd.melt(df, ignore_index=False).reset_index()
    
    # Set the variable order for plots
    varOrder = ['credit_freqFromProjects','credit_freqForTasks','satis_medium',
             'satis_taskFreq', 'credit_importance', 'freq_seenBy2',
             'freq_seenBy1', 'freq_seenBy0']
    
    # Plot the data as a pointplot
    sns.set_theme(style="white")
    sns.pointplot(data=df, x='value', y='variable',
                  order=varOrder, join=False)
    
    # Plot the data as a histogram/bargraph
    g = sns.FacetGrid(df, col='variable', col_wrap=4, col_order=varOrder)
    g.map(sns.histplot, 'value', discrete=True,
          kde=True, kde_kws={'bw_adjust': 2}, palette='mako')
    
def explore_means_split():
    
    # Load survey data
    df = io.load_survey_df()
    
    # Load numeric variables
    numVars = uv.get_variables_numeric()
    
    # Get order
    displayOrder = pd.Series(
        data=df.loc[:,('order','text','unified')].values,
        index=df.index,
        name='order'
        )
    
    # Slice down to just numeric and unified data
    df = df.xs(('numeric', 'unified'), level=(1,2), axis=1)
    
    # Now slice to just numeric variables
    df = df.loc[:,numVars]
    
    # Replace I'm not sure's with nans
    df = df.replace(6,nan)
    
    # Adjust value range for freq_seenBy2 (subtract 16)
    df.freq_seenBy2 = df.freq_seenBy2 - 16
    
    # Adjust value range for credit_importance (subtract 27)
    df.credit_importance = df.credit_importance - 27
    
    # Add displayOrder back in
    df = pd.merge(left=displayOrder,right=df,left_index=True, right_index=True)
    
    # Melt from wide to long
    df = df.melt(id_vars=['order'],ignore_index=True)
    
    # Set the variable order for plots
    varOrder = [
        'credit_freqFromProjects', 'credit_freqForTasks', 'satis_medium',
        'satis_taskFreq', 'credit_importance',
        'freq_seenBy2', 'freq_seenBy1', 'freq_seenBy0'
    ]

    # Plot the data as a pointplot
    sns.set_theme(style="white")
    sns.pointplot(data=df, x='value', y='variable', hue='order',
                  order=varOrder, join=False, dodge=True)
    
    # Plot the data as a histogram/bargraph
    g = sns.FacetGrid(df, col='variable', hue='order', col_wrap=4, col_order=varOrder)
    g.map(sns.histplot, 'value', discrete=True,
          kde=True, kde_kws={'bw_adjust': 2})
    g.add_legend()
    
    
    # Plot the order effects with regressions
    fig = plt.figure()
    ax = fig.gca()
    varOrder = ['freq_seenBy2', 'freq_seenBy1', 'freq_seenBy0', 'credit_importance']
    sns.pointplot(data=df, x='variable', y='value', hue='order', ax=ax,
                  order=varOrder, dodge=True)

if __name__ == '__main__':
    explore_means_split()
