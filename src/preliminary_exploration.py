# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:20:23 2022

@author: Juango the Blue
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


file = '../data/OSCS_20220629.csv'
df = pd.read_csv(file)
df = df.loc[2:,:]
df.rename(columns={'Path1-LaborVisibility_DO':'Order'},inplace = True)
df = df.replace({
    'Q28|Q11|Q12|Q13':'Decreasing (2,1,0)',
    'Q28|Q13|Q12|Q11':'Increasing (0,1,2)'
    })

#%% Histograms
sns.set_theme()
df2 = pd.melt(
    df,
    id_vars='Order',
    value_vars=['Q11','Q12','Q13'],
    var_name='Question'
    )

response_order = ['5 - Always','4 - Often','3 - Sometimes','2 - Rarely',
                  '1 - Never','nan', "I'm not sure"]
df3 = df2

# Create histograms
df2.value = pd.Categorical(df2.value,response_order)
g1 = sns.displot(
    data=df2,
    kind='hist',
    y='value',
    hue='Order',
    col='Question'
    )
sns.move_legend(g1,'lower center',bbox_to_anchor=(.5, 0),
                ncol=2, title=None, frameon=False, prop={'size': 12})
axes = g1.axes.flatten()
num_people = ['2 or more','Only 1','Nobody else']
for ax, title in zip(axes, num_people):
    ax.set_title(title)
plt.tight_layout(rect=(0,0.05,1,1))
g1.savefig('../figures/explore_visibility.png',dpi=300)

#%% ANOVA
sns.set_theme(style="whitegrid")
replace_dict = {
    '1 - Never':1,
    '2 - Rarely':2,
    '3 - Sometimes':3,
    '4 - Often':4,
    '5 - Always':5
    }
df3 = df3.replace(replace_dict)
df3.value = pd.to_numeric(df3.value, errors='coerce')
g2 = sns.catplot(data=df3, x='Question', y='value', hue='Order', kind='point')
g2.set_xticklabels(num_people)
g2.savefig('../figures/visibility_means.png',dpi=300)
