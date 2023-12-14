# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:45:57 2023

@author: jmeluso
"""

import plot_labor_categories as plc
import plot_compensation as pcomp
import plot_visibility as pv
import plot_correlation as pcorr
import plot_importance_regression as pir


def run_plots():
    
    # Create figure 1
    plc.plot_categorical()
    
    # Create figure 2
    pcomp.plot_compensation()
    
    # Create figure 3
    pv.plot_visibility_orders()
    
    # Create figure 4
    pcorr.plot_correlation()
    
    # Create figure 5
    pir.plot_importance_regression()


if __name__ == '__main__':
    run_plots()
