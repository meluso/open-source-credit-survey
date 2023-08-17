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
