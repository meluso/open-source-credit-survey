# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 16:13:07 2023

@author: jmeluso
"""

import itertools as it
import matplotlib.ticker as mtick
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import util.fig_settings as fs
import util.io as io
import util.plot as up
import util.variables as uv

def category_means(catgroup, question, sort=False, total=142):
    
    # Load survey data as a dictionary
    dtype2layout2df = io.load_survey_dict()
    
    # Load categorical variable group
    catgroup2group = uv.get_question_groups()
    group = catgroup2group[catgroup]
    df_cat = dtype2layout2df['numeric']['split'].loc[:,group]
    
    # Load question variable and null our "I'm not sure" responses
    df_question = dtype2layout2df['numeric']['unified'].loc[:,question]
    df_question = df_question.replace(6,np.nan)
    
    # Merge the categorical and question data
    df = pd.merge(df_cat, df_question, left_index=True, right_index=True)
    
    # Multiply out the question data
    for cat in group:
        df.loc[:,cat] = df.loc[:,cat].multiply(df.loc[:,question])
    
    # drop extra column that was merged
    df = df.loc[:,group]
    
    # Melt the values 
    df = pd.melt(df,value_vars=group)
    
    # Plot with seaborn
    fig = plt.figure(layout='tight')
    ax = fig.gca()
    sns.pointplot(data=df, x='value', y='variable', errorbar='ci', ax=ax)


def plot_category_means():
    
    # Load categorical and numeric variables
    catVars = uv.get_variables_categorical()
    numVars = uv.get_variables_numeric()
    
    for cat, num in it.product(catVars, numVars):
        category_means(cat, num)

if __name__ == '__main__':
    plot_category_means()
