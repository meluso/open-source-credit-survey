# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:14:15 2023

@author: jmeluso
"""
import numpy as np
from numpy import nan
import matplotlib.pyplot as plt
from matplotlib.patches import ArrowStyle, ConnectionPatch, Rectangle
from matplotlib import ticker
import seaborn as sns

import util.analysis as ua
import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()

def create_rectangle(ax, x, y, width, height, text, text_position, box_color,
                     text_color, text_size=10):
    # ax: a matplotlib axes object
    # x, y: the lower left corner coordinates of the rectangle
    # width, height: the width and height of the rectangle
    # text: the text to be displayed inside or above the rectangle
    # text_position: either 'center' or 'top'
    # box_color: the color of the rectangle
    # text_color: the color of the text
    # text_size: the size of the font

    # create a rectangle patch
    rect = Rectangle((x, y), width, height, facecolor=box_color)
    
    # add the patch to the axes
    ax.add_patch(rect)
    
    # calculate the text coordinates
    if text_position == 'center':
        
        # center the text inside the rectangle
        text_x = x + width / 2
        text_y = y + height / 2
        
    elif text_position == 'top':
        
        # place the text above the rectangle
        text_x = x + width / 2
        text_y = y + height + 0.05 # add some margin
        
    else:
        
        # invalid text position
        raise ValueError("text_position must be either 'center' or 'top'")
        
    # add the text to the axes
    ax.text(text_x, text_y, text, color=text_color, ha='center', va='center',
            size=text_size)
    

def plot_invisible_labor(ax):
    
    # Add title
    ax.set_title('(a) Labor becomes Invisible Labor when:', size=14, pad=31)
    
    # Remove borders and ticks
    fs.set_border(ax)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    
    # List out rectangles
    rects = {
        "Labor Data Isn't Visible": dict(
            x=0,
            y=0,
            width=0.42,
            height=1,
            text_position='top',
            box_color='#DDDDDD',
            text_color='#222222',
            text_size=12
            ),
        "Labor Is Undercompensated": dict(
            x=0.58,
            y=0,
            width=0.42,
            height=1,
            text_position='top',
            box_color='#DDDDDD',
            text_color='#222222',
            text_size=12
            ),
        "Doesn't Exist": dict(
            x=0.05,
            y=0.7,
            width=0.32,
            height=0.2,
            text_position='center',
            box_color='#666666',
            text_color='#FFFFFF'
            ),
        "Isn't Shared": dict(
            x=0.05,
            y=0.4,
            width=0.32,
            height=0.2,
            text_position='center',
            box_color='#666666',
            text_color='#FFFFFF'
            ),
        "Isn't Accessible": dict(
            x=0.05,
            y=0.1,
            width=0.32,
            height=0.2,
            text_position='center',
            box_color='#666666',
            text_color='#FFFFFF'
            ),
        "Doesn't Receive\nCredit": dict(
            x=0.63,
            y=0.7,
            width=0.32,
            height=0.2,
            text_position='center',
            box_color='#666666',
            text_color='#FFFFFF'
            ),
        "Doesn't Receive\nPay": dict(
            x=0.63,
            y=0.4,
            width=0.32,
            height=0.2,
            text_position='center',
            box_color='#666666',
            text_color='#FFFFFF'
            ),
        "No New\nOpportunities": dict(
            x=0.63,
            y=0.1,
            width=0.32,
            height=0.2,
            text_position='center',
            box_color='#666666',
            text_color='#FFFFFF'
            ),
        }
    
    # Create rectangles
    for text, values in rects.items():
        create_rectangle(ax, text=text, **values)   
        
    # List out other texts
    labels = [
        dict(x=0.21,y=0.95,s='because it',color='#222222',size=10),
        dict(x=0.21,y=0.65,s='or',color='#222222',size=10),
        dict(x=0.21,y=0.35,s='or',color='#222222',size=10),
        dict(x=0.5,y=0.95,s='or',color='#222222',size=13),
        dict(x=0.79,y=0.95,s='because it',color='#222222',size=10),
        dict(x=0.79,y=0.65,s='or',color='#222222',size=10),
        dict(x=0.79,y=0.35,s='or',color='#222222',size=10),
        dict(x=0.79,y=0.05,s='among others',color='#222222',size=10),
        ]
            
    # Add the text to the axes
    for label in labels:
        ax.text(ha='center', va='center', **label)


def plot_visibility_credit(ax):
    
    # Import survey dataframe
    df = io.load_survey_df()

    # Generate color palette
    # ['#332345', '#40498e', '#357ba3', '#38aaac', '#79d6ae']
    barColors = sns.color_palette('mako', n_colors=5).as_hex()
    labelColors = ['#FFFFFF','#FFFFFF','#FFFFFF','#FFFFFF','#222222']
    
    # Load question groups
    question2group = uv.get_question_groups()
    
    # Set questions to slice down to, and values for those vars to replace
    visVars = {
        'freq_seenBy0': 6,
        'freq_seenBy1': 6,
        'freq_seenBy2': 6,
        }
    
    # Slice down to numeric unified data for visibility questions
    dfVis = df.loc[:,([key for key in visVars.keys()], 'numeric', 'unified')]
    dfVis = dfVis.droplevel([1,2], axis=1)
    
    # Replace "I'm not sure" responses with nan
    dfVis = dfVis.replace(visVars, nan)
    
    # Normalize columns
    dfVis = ua.normalize_columns(dfVis)
    
    # Construct Visibility column
    visSeries = dfVis.mean()/sum(dfVis.mean())
    visValues = [
        visSeries[0], 0, visSeries[1], 0, visSeries[2]
        ]
    visLabels = [
        f'Invisible\n1 in 3 ({visValues[0]:.01%})',
        '',
        f'Partially\nVisible\n1 in 3 ({visValues[2]:.01%})',
        '',
        f'Visible\n1 in 3 ({visValues[4]:.01%})',
        ]
    
    # Slice down to numeric split data for credit questions
    dfCred = df.loc[:,(question2group['credit_freqFromProjects'], 'numeric', 'split')]
    dfCred = dfCred.droplevel([1,2], axis=1)
    
    # Drop "I'm not sure" responses
    dfCred = dfCred.iloc[:,0:5]
    
    # Construct Credit column
    credSeries = dfCred.count()/sum(dfCred.count())
    credValues = credSeries.values
    credLabels = [
        f'None\n1 in 10 ({credValues[0]:.01%})',
        f'A Few\n1 in 5 ({credValues[1]:.01%})',
        f'Some\n1 in 5 ({credValues[2]:.01%})',
        f'Most\n3 in 10 ({credValues[3]:.01%})',
        f'All\n1 in 10 ({credValues[4]:.01%})'
        ]
    
    # Loop through values for plot
    bottom = np.zeros(2)
    for vv, vl, cv, cl, bc, lc in zip(visValues, visLabels, credValues, \
        credLabels, barColors, labelColors):
        
        # Current values and labels to plot
        heights = (vv, cv)
        labels = (vl, cl)
        
        # Plot the bars
        bar = ax.bar(
            x = ('Labor Visibility', 'Credit from Projects'),
            height = heights,
            width = 0.7,
            bottom = bottom,
            color = bc
            )
        
        # Increment bottoms
        bottom += heights
        
        # Add labels
        ax.bar_label(
            container=bar,
            labels=labels,
            color=lc,
            label_type='center'
            )
    
    # Set tick formats
    ax.set_ylim(0,1)
    ax.yaxis.set_major_formatter(ticker.PercentFormatter(1))
    ax.tick_params(labeltop=True, labelbottom=False, bottom=False, labelsize=12)
    
    # Add title
    ax.set_title('(b) In OSS Ecosystems:', size=14, pad=15)
        
    # Remove borders
    fs.set_border(ax, left=True)

    
def plot_conceptual_overview(save=True):
    
    # Create figure
    fig, axs = plt.subplots(
        nrows=1, ncols=2, figsize=fs.fig_size(1, 0.4),
        dpi=600, layout='constrained',
        width_ratios=[3,2],
        gridspec_kw={'wspace': 0.15}
        )
    
    # Plot Invisible labor definition
    plot_invisible_labor(axs[0])
    
    # Plot arrow inbetween
    arrow = ConnectionPatch(
        xyA=(1.07,0.5), coordsA=axs[0].transData,
        xyB=(-0.8,0.5), coordsB=axs[1].transData,
        # Default shrink parameter is 0 so can be omitted
        color='#666666',
        arrowstyle=ArrowStyle("simple"),
        mutation_scale=30,  # controls arrow head size
        linewidth=5,
        capstyle='butt',
        joinstyle='miter'
    )
    fig.patches.append(arrow)
    
    # Plot proportions
    plot_visibility_credit(axs[1])
    
    # Draw an arrow from one ax to the other
    
    # Save the figure
    if save: fs.save_publication_fig('conceptual_overview')
    
if __name__ == '__main__':
    plot_conceptual_overview()
