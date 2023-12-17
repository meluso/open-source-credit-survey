# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 17:44:50 2023

@author: jmeluso
"""

import statsmodels.stats.api as sms

def conf_int_mean(dataCol, **kwds):
    lower, upper = sms.DescrStatsW(dataCol).tconfint_mean(**kwds)
    return lower, upper

def conf_int_diff_means(dataCol1, dataCol2, **kwds):
    cm = sms.CompareMeans(sms.DescrStatsW(dataCol1), sms.DescrStatsW(dataCol2))
    lower, upper = cm.tconfint_diff(usevar='unequal', **kwds)
    return lower, upper

def calc_weighted_visibility(df):
    numerator = 0*df['freq_seenBy0'] + 0.5*df['freq_seenBy1'] \
        + 1*df['freq_seenBy2']
    denominator = df['freq_seenBy0'] + df['freq_seenBy1'] + df['freq_seenBy2']
    return numerator/denominator

def calc_mean_credit(df):
    numerator = 0*df['freq_seenBy0'] + 0.5*df['freq_seenBy1'] \
        + 1*df['freq_seenBy2']
    denominator = df['freq_seenBy0'] + df['freq_seenBy1'] + df['freq_seenBy2']
    return numerator/denominator

def normalize_columns(df):
    return (df-df.min())/(df.max()-df.min())
