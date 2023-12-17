# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:43:32 2023

@author: jmeluso
"""
from matplotlib.legend_handler import HandlerTuple
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns

import util.analysis as ua
import util.fig_settings as fs
import util.io as io
import util.variables as uv

fs.set_fonts()

def add_arrow(line, position=None, direction='right', size=15, color=None):
    """
    add an arrow to a line.

    line:       Line2D object
    position:   x-position of the arrow. If None, mean of xdata is taken
    direction:  'left' or 'right'
    size:       size of the arrow in fontsize points
    color:      if None, line color is taken.
    """
    if color is None:
        color = line.get_color()

    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if position is None:
        position = xdata.mean()
    # find closest index
    start_ind = np.argmin(np.absolute(xdata - position))
    if direction == 'right':
        end_ind = start_ind + 1
    else:
        end_ind = start_ind - 1

    line.axes.annotate('',
        xytext=(xdata[start_ind], ydata[start_ind]),
        xy=(xdata[end_ind], ydata[end_ind]),
        arrowprops=dict(arrowstyle="->", color=color),
        size=size
    )
    
    
def setup_data_structures():
    
    # Set questions to slice down to, and values for those vars to replace
    numVars = {
        'freq_seenBy2': {'offset': 16},
        'freq_seenBy1': {'offset': 0},
        'freq_seenBy0': {'offset': 0}
        # 'credit_importance': 27,
        }
    
    # Total number of survey responses
    total = 142
    
    # Load question groups
    question2group = uv.get_question_groups()
    
    # Load split data for groups of variables
    dtype2layout2df = io.load_survey_dict()
    
    # Create stats dataframe, replace 6's with nans, and calculate stats
    statsDf = dtype2layout2df['numeric']['unified']
    stats = statsDf.replace(6,np.nan).describe()
    
    # Build the dataframe with the text order column on the end
    df = pd.concat([
        dtype2layout2df['numeric']['split'],
        dtype2layout2df['text']['unified']['order']],
        axis=1
        )
    
    # Load option definitions
    optionDefs = uv.get_option_definitions()
    
    # Generate color palette
    colors = sns.color_palette('mako', n_colors=2).as_hex()
    
    # Create a list of the order options
    orderOpts = pd.Series(df.order.dropna().unique())
    
    return numVars, total, question2group, dtype2layout2df, statsDf, stats, \
        df, optionDefs, colors, orderOpts
        
        
def setup_figure(nrows, subfig, **kwds):
    
    # Create a figure from a subfigure
    fig = subfig
    axs = fig.subplots(nrows=nrows, ncols=1,**kwds)
        
    return fig, axs


def plot_means(subfig, otherHandles, overall_mean=False):
    
    # Load the variables, dataframe, dictionaries
    numVars, total, question2group, dtype2layout2df, statsDf, stats, \
        df, optionDefs, colors, orderOpts = setup_data_structures()
    
    # Create a figure with 2 axes
    fig, axs = setup_figure(nrows=2, subfig=subfig, height_ratios=[5,1])
    ax = axs[0] # For means
    axLegend = axs[1] # For legend
    
    # Create a dictionary to store the means by variable
    orders = [oo for oo in orderOpts] + ['overall']
    statsNames = ['mean', 'ciLo', 'ciHi']
    order2statDf = {
        oo: pd.DataFrame(index=numVars.keys(), columns=statsNames)
        for oo in orders
        }
    
    # Add gray to the colors
    colors = [color for color in colors]
    colors.append('#666666')
    
    # Loop through the variables and order options
    for var in numVars:
        
        # Create stats dataframe, and subtract offsets as needed
        answers = dtype2layout2df['numeric']['unified'][var].replace(6,np.nan)
        answers = answers - numVars[var]['offset']
        answers = answers.dropna()
        
        # Calculate the mean and confidence interval
        order2statDf['overall'].loc[var,'mean'] = answers.mean()
        
        # Calculate the confidence interval
        ciLo, ciHi = ua.conf_int_mean(answers)
        order2statDf['overall'].loc[var,'ciLo'] = ciLo
        order2statDf['overall'].loc[var,'ciHi'] = ciHi
        print(f'({var},overall):\t\t{ciLo:.3}, {answers.mean():.3}, {ciHi:.3}')
        
        # Loop through the order options
        for oo in orderOpts:
            
            # Slice down to the order subset
            subset = answers[df['order'] == oo]
            subset = subset.dropna()
            
            # Calculate the mean and confidence interval
            order2statDf[oo].loc[var,'mean'] = subset.mean()
            
            # Calculate the confidence interval
            ciLo, ciHi = ua.conf_int_mean(subset.dropna())
            order2statDf[oo].loc[var,'ciLo'] = ciLo
            order2statDf[oo].loc[var,'ciHi'] = ciHi
            print(f'({var},{oo}):\t\t{ciLo:.3}, {subset.mean():.3}, {ciHi:.3}')
        
    # Set alpha
    alpha = 1
            
    # Loop through the orders for plotting
    for ii, (oo, color) in enumerate(zip(orderOpts, colors)):
        
        # Set the values for plotting
        x = order2statDf[oo]['mean']
        y = np.array([2,1,0]) - 0.025 + ii*0.05
        xerr = (
            order2statDf[oo]['mean'] - order2statDf[oo]['ciLo'],
            order2statDf[oo]['ciHi'] - order2statDf[oo]['mean']
            )
            
        # Plot the means on the axes
        lines = ax.plot(x, y, label=oo, color=color, marker='.', ms=10, zorder=3, alpha=alpha)
        
        # Plot the confidence intervals on the axes
        ax.errorbar(
            x, y,
            xerr=xerr,
            color=color,
            capsize=5,
            alpha=alpha
            )
        
        # Get line and xdata for adding arrows
        line = lines[0]
        xdata = line.get_xdata()
        ydata = line.get_ydata()
        
        # Specify arrow direction
        if oo == 'Visibility ($\geq$2,1,0)':
            start = 18/24
            end = 19/24
        else:
            start = 6/24
            end = 5/24
        
        # Loop through all but the last index
        for ii, (xx,yy) in enumerate(zip(xdata[:-1],ydata[:-1])):
            
            # Calculate the 2/3 point of each segment
            xStart = start*(xdata[ii+1] - xdata[ii]) + xdata[ii]
            xEnd = end*(xdata[ii+1] - xdata[ii]) + xdata[ii]
            yStart = start*(ydata[ii+1] - ydata[ii]) + ydata[ii]
            yEnd = end*(ydata[ii+1] - ydata[ii]) + ydata[ii]
            
            # Now draw the arrow at that position
            line.axes.annotate('',
                xytext=(xStart, yStart),
                xy=(xEnd, yEnd),
                arrowprops=dict(arrowstyle="->", color=line.get_color(), alpha=alpha),
                size=15
            )
    
    # Plot overall means
    if overall_mean:
        
        oo = 'overall'
        x = order2statDf[oo]['mean']
        y = np.array([2,1,0])
        xerr = (
            order2statDf[oo]['mean'] - order2statDf[oo]['ciLo'],
            order2statDf[oo]['ciHi'] - order2statDf[oo]['mean']
            )
            
        # Plot the means on the axes
        lines = ax.plot(x, y, label=oo, color=colors[2], marker='.', ms=10, zorder=3)
        
        # Plot the confidence intervals on the axes
        ax.errorbar(
            x, y,
            xerr=xerr,
            color=colors[2],
            capsize=5,
            )
    
    # Add title
    ax.set_title(f'(a) Response means by visibility anchoring')
        
    # Set the x limits
    ax.set_xlim((1.8,4.2))
    ax.set_ylim((-0.25,2.25))
        
    # Update x labels
    xTickVars = question2group[var][1:4]
    ax.xaxis.set_major_locator(mtick.FixedLocator(range(2,5)))
    ax.set_xticklabels(
        labels=[optionDefs[var] for var in xTickVars],
        rotation=-45, ha='left', rotation_mode='anchor'
        )
    
    # Update y labels
    ax.yaxis.set_major_locator(mtick.FixedLocator(range(len(numVars))))
    ax.set_yticklabels(
        labels=[
            'Invisible\n(0 people)',
            'Partially\nVisible\n(1 person)',
            'Visible\n($\geq2$ people)'
            ]
        )        
        
    # Remove borders
    fs.set_border(ax, bottom=True)
    
    # Add grid
    ax.grid(axis='x')
    ax.set_axisbelow(True)
    
    # Create the handles
    theseHandles, labels = ax.get_legend_handles_labels()
    handles = [(th,oh) for th,oh in zip(theseHandles, otherHandles)]
    
    # Now create the legend
    legend = axLegend.legend(handles, labels,
                             handler_map={tuple: HandlerTuple(ndivide=None)},
                             loc='lower right', columnspacing=1,
                             labelspacing=0.2, frameon=False,
                             )
    fs.set_border(axLegend)
    axLegend.tick_params(axis='both',which='both',bottom=False,left=False)
    axLegend.set_xticklabels([])
    axLegend.set_yticklabels([])
    
    # Adjust legend title
    title = axLegend.text(x=0, y=0.5, s='Anchored to...')


def plot_distributions(subfig):
    
    # Load the variables, dataframe, dictionaries
    numVars, total, question2group, dtype2layout2df, statsDf, stats, \
        df, optionDefs, colors, orderOpts = setup_data_structures()
    
    # Create a figure with 3 axes
    fig, axs = setup_figure(nrows=len(numVars), subfig=subfig, sharex=True)
    
    # Cycle through axes (flat) and populate them for each variable
    for ii, (var, ax, letter) in enumerate(zip(numVars, axs.flat, 'bcd')):
        
        # Get the variable's group
        group = question2group[var]
        
        # Create stats dataframe, and subtract offsets as needed
        statsDf = dtype2layout2df['numeric']['unified'][var].replace(6,np.nan)
        statsDf = statsDf - numVars[var]['offset']
        
        # Save the variable's overall mean, low and high bounds
        numVars[var]['mean'] = statsDf.mean()
        ciLo, ciHi = ua.conf_int_mean(statsDf.dropna())
        numVars[var]['mean_lo'] = ciLo
        numVars[var]['mean_hi'] = ciHi
        
        # Create list of errorbar centers
        xCenters = []
        yCenters = []
        
        # Loop through the variables and colors
        for jj, (oo, color) in enumerate(zip(orderOpts, colors)):
            
            # Slice down data to variable subset
            data = df.loc[df['order'] == oo,group]
            
            # Get the fraction of respondents who gave each response
            percents = data.sum()/total
            
            # Calculate stats for current order option
            stats = statsDf[df['order'] == oo].describe()
            
            # Calculate and save the errorbar points
            y = 0.21 + jj*0.02
            x = stats['mean'] - 1
            xCenters.append(x)
            yCenters.append(y)
            
            # Plot the percents
            ax.bar(
                x=-0.1+jj*0.2+np.arange(len(percents)),
                height=percents,
                color=color,
                alpha=0.75,
                width=0.7,
                label=oo
                )
        
        # Add title
        ax.set_title(f'({letter}) Response distribution: {optionDefs[var]}')
        
        # Set y limits
        ax.set_ylim((0,0.22))
        
        # Update x labels
        ax.xaxis.set_major_locator(mtick.FixedLocator(range(len(percents))))
        ax.set_xticklabels([optionDefs[index] for index in percents.index],
                           rotation=-45, ha='left', rotation_mode='anchor')
        
        # Update y labels
        ax.yaxis.set_major_locator(mtick.MaxNLocator(5))
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
        
        # Remove borders
        fs.set_border(ax, bottom=True)
        
        # Add grid
        ax.grid(True)
        ax.set_axisbelow(True)
        
    # Return the handles
    handles, labels = ax.get_legend_handles_labels()
    return handles


def plot_visibility_orders(save=True):
        
    # Create base figure and grid
    fig = plt.figure(figsize=fs.fig_size(1, 0.4), layout='constrained')
    subfigs = fig.subfigures(nrows=1, ncols=2, wspace=0)
    
    # Create the distributions figure on the right, without a legend
    handles = plot_distributions(subfigs[1])
    
    # Create the means figure on the left, with the legend
    plot_means(subfigs[0], handles)
    
    # Save the plot!
    if save: fs.save_publication_fig('visibility', bbox_inches='tight')
    
    
if __name__ == '__main__':
    plot_visibility_orders()
