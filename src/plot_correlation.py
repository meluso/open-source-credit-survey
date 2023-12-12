# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:41:14 2023

@author: jmeluso
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
import pandas as pd
import scipy.cluster.hierarchy as sch
from scipy.stats import pearsonr
import seaborn as sns
from string import ascii_uppercase

import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()

def cluster_corr(corr_array, inplace=False):
    """
    Rearranges the correlation matrix, corr_array, so that groups of highly 
    correlated variables are next to eachother 
    
    Parameters
    ----------
    corr_array : pandas.DataFrame or numpy.ndarray
        a NxN correlation matrix 
        
    Returns
    -------
    pandas.DataFrame or numpy.ndarray
        a NxN correlation matrix with the columns and rows rearranged
    """
    pairwise_distances = sch.distance.pdist(corr_array)
    linkage = sch.linkage(pairwise_distances, method='complete')
    cluster_distance_threshold = pairwise_distances.max()/2
    idx_to_cluster_array = sch.fcluster(linkage, cluster_distance_threshold, 
                                        criterion='distance')
    idx = np.argsort(idx_to_cluster_array)
    
    if not inplace:
        corr_array = corr_array.copy()
    
    if isinstance(corr_array, pd.DataFrame):
        return corr_array.iloc[idx, :].T.iloc[idx, :]
    return corr_array[idx, :][:, idx]


def plot_correlation():
    
    # Import survey dataframe
    df = io.load_survey_df()
    
    # Set questions to slice down to, and values for those vars to replace
    keepVars = {
        'credit_freqForTasks': 6,
        'credit_freqFromProjects': 6,
        'credit_importance': nan,
        'freq_seenBy0': 6,
        'freq_seenBy1': 6,
        'freq_seenBy2': 6,
        'satis_medium': nan,
        'satis_taskFreq': nan,
        'order': nan,
        }
    
    # Slice down to numeric unified data
    df = df.loc[:,([key for key in keepVars.keys()], 'numeric', 'unified')]
    df = df.droplevel([1,2], axis=1)
    
    # Replace "I'm not sure" responses with nan
    df = df.replace(keepVars, nan)
    
    # Import variable (option) definitions
    names = uv.get_option_definitions()
    
    # Calculate correlation
    corr = df.corr(
        method=lambda x, y: pearsonr(x, y)[0])
    
    # Sort everything by average correlations
    corr = cluster_corr(corr)
    df = df.reindex(corr.columns, axis=1)
    
    # Caluclate pvalues
    pvalues = df.corr(
        method=lambda x, y: pearsonr(x, y)[1]) - np.eye(len(df.columns))
    
    # Generate a mask for the upper triangle and insignificant p-values
    mask_signif = np.triu(np.ones_like(corr, dtype=bool)) + (pvalues>0.05)
    mask_notsig = np.triu(np.ones_like(corr, dtype=bool)) + (pvalues<=0.05)
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=fs.fig_size(1, 0.3), dpi=600)
    
    # Generate a diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    # Draw the heatmap with the mask and correct aspect ratio
    ax = sns.heatmap(corr,
        mask=mask_signif, center=0, cmap=cmap, square=True, ax=ax, 
        linewidths=0.5, annot=corr, vmin=-0.85, vmax=0.85, fmt='.2f', 
        cbar_kws={"shrink": 1}, annot_kws={'size': 8}
        )
    
    # Draw a second heatmap (for convience) with all grayed out insignificants
    ax = sns.heatmap(mask_notsig-0.6,
        mask=mask_notsig, center=0, cmap='Greys', square=True, ax=ax, 
        linewidths=0.5, annot=corr, vmin=-0.85, vmax=0.85, fmt='.2f', 
        cbar=False, annot_kws={'size': 8}
        )
    
    # Get the strings for the x & y tick labels
    labels = zip(
        [names[tick.get_text()] for tick in ax.get_yticklabels()],
        ascii_uppercase
    )
    
    # Construct the x & y tick labels
    xticklabels, yticklabels = [], []
    for name, letter in labels:
        yticklabels.append(f'{name} - {letter}')
        xticklabels.append(letter)
    
    # Set the tick labels
    ax.set_xticklabels(xticklabels, rotation=0)
    ax.set_yticklabels(yticklabels)
    
    # Save the figure
    fs.save_publication_fig('correlation_matrix')
    

if __name__ == '__main__':
    
    plot_correlation()
