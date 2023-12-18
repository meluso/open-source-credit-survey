# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:14:15 2023

@author: jmeluso
"""

from numpy import nan
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
import statsmodels.formula.api as smf

import util.analysis as ua
import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()

def plot_visibility_vs_credit(ax):
    
    # Import survey dataframe
    df = io.load_survey_df()
    
    # Set questions to slice down to, and values for those vars to replace
    keepVars = {
        'order': nan,
        'credit_freqForTasks': 6,
        'credit_freqFromProjects': 6,
        'freq_seenBy0': 6,
        'freq_seenBy1': 6,
        'freq_seenBy2': 6,
        'credit_importance': nan
        }
        
    # Load question group
    question2group = uv.get_question_groups()
    
    # Generate color palette
    colors = sns.color_palette('mako_r', n_colors=2).as_hex()
    
    # Slice down to numeric unified data
    df = df.loc[:,([key for key in keepVars.keys()], 'numeric', 'unified')]
    df = df.droplevel([1,2], axis=1)
    
    # Replace "I'm not sure" responses with nan
    df = df.replace(keepVars, nan)
    
    # Normalize columns
    df = ua.normalize_columns(df)
    
    # Calculate average visibility and credit
    df['visibility_mean'] = ua.calc_weighted_visibility(df)
    df['credit_mean'] = (df['credit_freqForTasks'] + df['credit_freqFromProjects'])/2
    
    # Calculate correlation between average visibility and average credit
    corr = df[['visibility_mean','credit_mean']].corr()\
        .loc['visibility_mean','credit_mean']
    print(f'Visibility-Credit Correlation: r={corr:.2}')
    
    # Import variable (option) definitions
    names = uv.get_option_definitions()
    
    # Create regression plot
    sns.regplot(
        data=df,
        x="credit_mean",
        y="visibility_mean",
        scatter_kws={'color': colors[0], 'alpha':0.3},
        line_kws={'color': colors[1]},
        ax=ax
        )
    
    # Set limits
    limits = (-0.05,1.05)
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    
    # Update ticks & labels
    ax.xaxis.set_major_locator(ticker.FixedLocator(
        [0,0.25,0.5,0.75,1]
        ))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter([
        '0\nNever\nCredited',
        '',
        '0.5\n',
        '',
        '1\nAlways\nCredited'
        ]))
    ax.yaxis.set_major_locator(ticker.FixedLocator(
        [0,0.25,0.5,0.75,1]
        ))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter([
        'Invisible - 0',
        '',
        '0.5',
        '',
        'Visible - 1'
        ]))
    
    # Set labels
    ax.set_title('(a) Correlation: Visibility vs. credit frequency')
    ax.set_xlabel('Average Credit Frequency')
    ax.set_ylabel('Average Visibility')
        
    # Remove borders
    fs.set_border(ax)
    
    # Add grid
    ax.grid(True)
    ax.set_axisbelow(True)


def plot_importance_regression(ax):
    
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
    df = ua.normalize_columns(df)
    
    # Import variable (option) definitions
    names = uv.get_option_definitions()
    
    # Run regression
    results = smf.ols('credit_importance ~ order', data=df).fit(cov_type='HC2')
    print(results.summary())
    
    # Plot points and regression line
    sns.regplot(x='order',y='credit_importance', data=df,
        x_jitter=0.1, y_jitter=0.05, ax=ax, x_ci='ci', ci=95, seed=499,
        scatter_kws={'color': colors[1], 'alpha':0.3},
        line_kws={'color': colors[0]})
    
    # Set ticks
    
    # Update ticks & labels
    ax.xaxis.set_major_locator(ticker.FixedLocator(range(2)))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter([
        'Anchored to Visibility\n($\geq$2, 1, 0 people)\n',
        'Anchored to Invisibility\n(0, 1, $\geq$2 people)\n'
        ]))
    ax.yaxis.set_major_locator(ticker.FixedLocator(
        [0,0.25,0.5,0.75,1]
        ))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(
        [names[index] for index in group]
        ))
    
    # Update axis labels
    ax.set_title('(b) Regression: Credit importance on question order', loc='right')
    ax.set_xlabel('Visibility Question Order')
    ax.set_ylabel('Credit Importance')
    
    # Remove borders
    fs.set_border(ax)
    
    # Add grid
    ax.grid(True)
    ax.set_axisbelow(True)
    
def plot_variable_relationships(save=True):
    
    # Create figure
    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=fs.fig_size(1, 0.3),
                            dpi=600, layout='constrained',
                            gridspec_kw={'wspace': 0.1})
    
    # Plot visibility vs credit
    plot_visibility_vs_credit(axs[0])
    
    # Plot importance regression
    plot_importance_regression(axs[1])
    
    # Save the figure
    if save: fs.save_publication_fig('variable_relationships')
    
if __name__ == '__main__':
    plot_variable_relationships()
