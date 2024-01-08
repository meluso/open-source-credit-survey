# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:14:15 2023

@author: jmeluso
"""
import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib import ticker
import seaborn as sns

import util.analysis as ua
import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()
    

def plot_invisible_labor(ax):
    
    # Generate color palette and select the color for all bars
    colors = sns.color_palette('mako_r', n_colors=5).as_hex()
    colors = (colors[1],colors[3])
    
    # Add title
    ax.set_title('(a) Invisible Labor, Defined', size=14)
    
    # Remove borders ticks
    fs.set_border(ax)
    
    # Set limits
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    
    # Create ticks
    ax.xaxis.set_ticks(
        ticks=[0.5, 1.5],
        labels=['Partially or\nNot Visible','Fully Visible']
        )
    ax.yaxis.set_ticks(
        ticks=[0.5, 1.5],
        labels=['Under-\nCompensated','Appropriately\nCompensated']
        )
    
    # Add bounding lines
    ax.axhline(1, color='gray', linewidth=0.75)
    ax.axvline(1, color='gray', linewidth=0.75)
    
    # Create info for two polygons
    offset = 0.05
    group = {
        "Invisible Labor": [
            dict(x=1,y=0.6, color='#FFFFFF', size=16),
            dict(
                xy=[
                    (0+offset,2-offset),
                    (1-offset,2-offset),
                    (1-offset,1-offset),
                    (2-offset,1-offset),
                    (2-offset,0+offset),
                    (0+offset,0+offset)
                    ],
                color=colors[1]
                )
            ],
        "Not\nInvisible\nLabor": [
            dict(x=1.5,y=1.5, color='#FFFFFF', size=12),
            dict(
                xy=[
                    (1+offset,2-offset),
                    (2-offset,2-offset),
                    (2-offset,1+offset),
                    (1+offset,1+offset)
                    ],
                color='#AAAAAA'
                )
            ],
        }
    
    # Create the polygons
    for string, (loc, shape) in group.items():
        ax.add_patch(Polygon(**shape))
        ax.text(s=string,**loc, ha='center', va='center')
        
    # Create label props
    color='#AAAAAA'
    arrowprops=dict(arrowstyle='->',fc=color,ec=color)
    
    ## Left axis, bottom middle
    # Create less compensated label
    ax.annotate(text='', xy=(-0.05,0.75), xytext=(-0.05,1.25), 
        arrowprops=arrowprops, annotation_clip=False)
    ax.text(s='Less\nCompensated', x=-0.1, y=1, color=color, size=10,
            va='center', ha='right')
    
    # Create less visible label
    ax.annotate(text='', xy=(0.75,-0.3), xytext=(1.25,-0.3), 
        arrowprops=arrowprops, annotation_clip=False)
    ax.text(s='Less Visible', x=1, y=-0.25, ha='center', color=color, size=10)
    

def plot_visibility_credit(ax):
    
    # Import survey dataframe
    df = io.load_survey_df()
    
    # Load question groups
    question2group = uv.get_question_groups()
    
    # Set questions to slice down to, and values for those vars to replace
    visVars = {
        'freq_seenBy0': 6,
        'freq_seenBy1': 6,
        'freq_seenBy2': 6,
        }
    
    # Get Visibility values to Plot
    dfVis = df.loc[:,([key for key in visVars.keys()], 'numeric', 'unified')]
    dfVis = dfVis.droplevel([1,2], axis=1)
    dfVis = dfVis.replace(visVars, nan)
    dfVis = ua.normalize_columns(dfVis)
    visSeries = dfVis.mean()/sum(dfVis.mean())
    
    # Get compensation values to plot
    dfCred = df.loc[:,(question2group['credit_freqFromProjects'], 'numeric', 'split')]
    dfCred = dfCred.droplevel([1,2], axis=1)
    dfCred = dfCred.iloc[:,0:5]
    credSeries = dfCred.count()/sum(dfCred.count())    
    
    # Construct columns to plot
    vis_visValues = [visSeries[2], 0, 0, 0]
    invis_visValues = [visSeries[0], 0, visSeries[1], 0]
    vis_compValues = [credSeries.values[4], 0, 0, 0]
    invis_compValues = credSeries.values[0:4]
    
    # Construct labels
    vis_visLabels = [
        f'Fully\nVisible\n{vis_visValues[0]:.01%}',
        '',
        '',
        ''
        ]
    invis_visLabels = [
        f'Non-\nvisible\n{invis_visValues[0]:.01%}',
        '',
        f'Partially\nVisible\n{invis_visValues[2]:.01%}',
        ''
        ]
    vis_compLabels = [
        f'All\n{vis_compValues[0]:.01%}',
        '',
        '',
        ''
        ]
    invis_compLabels = [
        f'None\n{invis_compValues[0]:.01%}',
        f'A Few\n{invis_compValues[1]:.01%}',
        f'Some\n{invis_compValues[2]:.01%}',
        f'Most\n{invis_compValues[3]:.01%}',
        ]
    
    # Generate color palettes
    # Mako 5, second entry: #40498e (purple)
    vis_barColors = sns.light_palette('#AAAAAA',
        n_colors=4, reverse=True).as_hex()
    invis_barColors = sns.light_palette('#40498e',
        n_colors=6, reverse=True).as_hex()
    labelColors = ['#FFFFFF','#222222','#222222', '#222222']
    
    # Create x locations for 4 bars
    width = 0.4
    xlocs = [0 - width/2, 0 + width/2, 1 - width/2, 1 + width/2]
    bottom = np.zeros(4)
    
    # Create a zipper for 
    zipper = zip(
        vis_visValues, invis_visValues, vis_compValues, invis_compValues,
        vis_visLabels, invis_visLabels, vis_compLabels, invis_compLabels,
        vis_barColors, invis_barColors, labelColors
        )
    
    # Loop through values for plot
    for valVV, valIV, valVC, valIC, labVV, labIV, labVC, labIC, colVB, colIB, \
        colL in zipper:
        
        # Current values and labels to plot
        heights = (valVV, valIV, valVC, valIC)
        labels = (labVV, labIV, labVC, labIC)
        barColors = (colVB, colIB, colVB, colIB)
        
        # Plot the bars
        bar = ax.bar(
            x = xlocs,
            height = heights,
            width = width,
            bottom = bottom,
            color = barColors
            )
        
        # Increment bottoms
        bottom += heights
        
        # Add labels
        ax.bar_label(
            container=bar,
            labels=labels,
            color=colL,
            label_type='center'
            )
        
    # Add cap labels
    ax.bar_label(
        container=bar,
        labels=('','2 in 3 People','','9 in 10 People'),
        color='#222222',
        label_type='edge',
        size=12,
        padding=3
        )
    
    # Set x tick formats
    ax.xaxis.set_major_locator(ticker.FixedLocator([0,1]))
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(['Visibility','Compensation']))
    ax.xaxis.set_tick_params(labelsize=12)
    
    # Set y tick formats
    ax.set_ylim(0,1)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(1))
    
    # Add title
    ax.set_title('(b) In Open Source Ecosys.', size=14)
        
    # Remove borders
    fs.set_border(ax, left=True)

    
def plot_conceptual_overview(save=True):
    
    # Create figure
    fig, axs = plt.subplots(
        nrows=1, ncols=2, figsize=fs.fig_size(1, 0.4),
        dpi=600, layout='constrained',
        gridspec_kw={'wspace': 0.1}
        )
    
    # Plot Invisible labor definition
    plot_invisible_labor(axs[0])
    
    # Plot proportions
    plot_visibility_credit(axs[1])
    
    # Save the figure
    if save: fs.save_publication_fig('conceptual_overview')
    
if __name__ == '__main__':
    plot_conceptual_overview()
