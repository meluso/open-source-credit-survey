# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:45:57 2023

@author: jmeluso
"""

import plot_conceptual_overview as pco
import plot_labor_categories as plc
import plot_compensation as pcomp
import plot_visibility as pv
import plot_correlation as pcorr
import plot_variable_relationships as pvr


def run_plots():
    
    # Create figure 1
    pco.plot_conceptual_overview()
    
    # Create figure 2
    plc.plot_categorical()
    
    # Create figure 3
    pcomp.plot_compensation()
    
    # Create figure 4
    pv.plot_visibility_orders()
    
    # Create figure 5
    pcorr.plot_correlation()
    
    # Create figure 6
    pvr.plot_variable_relationships()


if __name__ == '__main__':
    run_plots()
