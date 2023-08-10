# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 16:14:05 2023

@author: jmeluso
"""

import csv
import pickle

def load_csv_to_dict(filename):

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = {}
        for row in reader:
            data[row[0]] = row[1]

    return data


def write_pickle(name, loc):

    with open(f'{name}.pickle', 'wb') as handle:
        pickle.dump(loc, handle, protocol=pickle.HIGHEST_PROTOCOL)
        

def read_pickle(name):

    with open(f'{name}.pickle', 'rb') as handle:
        b = pickle.load(handle)
    
    return b

def load_survey_df():
    df = read_pickle('../data/refined/responses_df')
    return df

def load_survey_dict():
    dataDict = read_pickle('../data/refined/responses_dict')
    return dataDict
