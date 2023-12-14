# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:53:54 2023

@author: jmeluso
"""

from numpy import nan
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
import statsmodels.formula.api as smf

import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()

def plot_importance_regression(save=True):
    
    # Import survey dataframe
    df = io.load_survey_df()
    
    # Set questions to slice down to, and values for those vars to replace
    keepVars = {
        'order': nan,
        'credit_importance': nan
        }
        
    # Load question group
    question2group = uv.get_question_groups()
    group = question2group['credit_importance']
    
    # Generate color palette
    colors = sns.color_palette('mako', n_colors=2).as_hex()
    
    # Slice down to numeric unified data
    df = df.loc[:,([key for key in keepVars.keys()], 'numeric', 'unified')]
    df = df.droplevel([1,2], axis=1)
    
    # Replace "I'm not sure" responses with nan
    df = df.replace(keepVars, nan)
    
    # Normalize columns
    df = (df-df.min())/(df.max()-df.min())
    
    # Import variable (option) definitions
    names = uv.get_option_definitions()
    
    # Run regression
    results = smf.ols('credit_importance ~ order', data=df).fit(cov_type='HC2')
    print(results.summary())
    
    # Create figure
    fig, ax = plt.subplots(figsize=fs.fig_size(0.35, 0.3), dpi=600)
    
    # Plot points and regression line
    sns.regplot(x='order',y='credit_importance', data=df,
        x_jitter=0.1, y_jitter=0.05, ax=ax, x_ci='ci', ci=95, seed=499,
        scatter_kws={'color': colors[1], 'alpha':0.3},
        line_kws={'color': colors[0]})
    
    # Set ticks
    
    # Update ticks & labels
    ax.xaxis.set_major_locator(ticker.FixedLocator(range(2)))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter([
        'Anchored to Visibility\n($\geq$2, 1, 0 people)',
        'Anchored to Invisibility\n(0, 1, $\geq$2 people)'
        ]))
    ax.yaxis.set_major_locator(ticker.FixedLocator(
        [0,0.25,0.5,0.75,1]
        ))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(
        [names[index] for index in group]
        ))
    
    # Update axis labels
    ax.set_xlabel('')
    ax.set_ylabel('Credit Importance')
    
    # Add grid
    ax.grid(True)
    # ax.set_axisbelow(True)
    
    # Remove borders
    fs.set_border(ax)
        
    # Save the plot
    if save: fs.save_publication_fig('importance_regression', bbox_inches='tight')
    
if __name__ == '__main__':
    plot_importance_regression()
