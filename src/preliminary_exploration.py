# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:20:23 2022

@author: Juango the Blue
"""

import pandas as pd
import seaborn as sns


file = 'OSCS_20220629.csv'
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

response_order = ['1 - Never','2 - Rarely','3 - Sometimes','4 - Often',
                  '5 - Always', 'nan', "I'm not sure"]
df3 = df2

# Create histograms
df2.value = pd.Categorical(df2.value,response_order)
g1 = sns.displot(
    data=df2,
    kind='hist',
    x='value',
    hue='Order',
    col='Question'
    )
g1.set_xticklabels(rotation=45)

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