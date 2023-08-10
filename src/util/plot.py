# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 18:07:13 2023

@author: jmeluso
"""    

def arrow(ax, xyfrom, xyto, text=''):
    an = ax.annotate(text=text, xy=xyto, xytext=xyfrom, annotation_clip=False,
        arrowprops=dict(arrowstyle='->',fc='#AAAAAA',ec='#AAAAAA'),
        xycoords='axes fraction')
    return an
