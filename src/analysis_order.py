# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:43:32 2023

@author: jmeluso
"""

from numpy import nan
from patsy import dmatrices
import statsmodels.api as sm

import util.io as io

def regression():
    
    # Load survey dataframe
    df = io.load_survey_df()
    
    # Set questions to slice down to, and values for those vars to replace
    keepVars = {
        'credit_importance': nan,
        'freq_seenBy0': 6,
        'freq_seenBy1': 6,
        'freq_seenBy2': 6,
        'order': nan,
        }
    
    # Slice down to numeric unified data
    df = df.loc[:,([key for key in keepVars.keys()], 'numeric', 'unified')]
    df = df.droplevel([1,2], axis=1)
    
    # Replace "I'm not sure" responses with nan
    df = df.replace(keepVars, nan)
    df = df.dropna()
    
    # Adjust value range for freq_seenBy2 (subtract 16)
    df.freq_seenBy2 = df.freq_seenBy2 - 16
    
    # Adjust value range for credit_importance (subtract 27)
    df.credit_importance = df.credit_importance - 27
    
    # Normalize columns
    for col in df.columns:
        df[col] = (df[col] - df[col].min())/(df[col].max() - df[col].min())
    
    # Build regression columns
    y, X = dmatrices('credit_importance ~ order', data=df, return_type='dataframe')
    
    # Build model, fit, and summarize
    mod = sm.OLS(y, X)
    results = mod.fit()
    print(results.summary())
    
    # Build regression columns
    y, X = dmatrices('freq_seenBy0 ~ order', data=df, return_type='dataframe')
    
    # Build model, fit, and summarize
    mod = sm.OLS(y, X)
    results = mod.fit()
    print(results.summary())
    
    # Build regression columns
    y, X = dmatrices('freq_seenBy1 ~ order', data=df, return_type='dataframe')
    
    # Build model, fit, and summarize
    mod = sm.OLS(y, X)
    results = mod.fit()
    print(results.summary())

    
    
if __name__ == '__main__':
    regression()
