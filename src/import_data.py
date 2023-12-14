# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:39:30 2023

@author: jmeluso
"""

import itertools as it
import pandas as pd
import util.io as io
import util.variables as uv

def ingest_survey_data():
    
    # Create a dictionary of the file locations
    dtypes = ['numeric', 'text']
    layouts = ['split','unified']
    
    # Specify rows and columns to remove from the datasets
    rowsToRemove = [0,1]
    colsToRemove = [
        'StartDate','EndDate','Status','Progress',
        'Duration (in seconds)','Finished','RecordedDate','ResponseId',
        'DistributionChannel','UserLanguage'
        ]
    
    # Construct a dictionary to store survey results
    dataDict = {dtype: {} for dtype in dtypes}
    
    # Construct a dataframe to store survey results
    df_all = pd.DataFrame()
    
    # Iterate through each of the csv files
    for dtype, layout in it.product(dtypes, layouts):
        
        location = f'../data/raw/OSCS_{dtype}{layout.title()}.csv'
        
        # Load the data group from the location with pandas
        df = pd.read_csv(location)
        
        # Remove unneeded rows & columns from dataframe
        df = df.drop(index=rowsToRemove, columns=colsToRemove)
        
        # Convert the datatypes of the columns as appropriate
        if dtype == 'numeric':
            
            # Replace order strings numerically
            df = df.replace({
                'Q28|Q11|Q12|Q13': 2,
                'Q28|Q13|Q12|Q11': 4
                })
            
            # Convert the datatypes of columns to numeric
            for col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
                
        else:
            
            # Replace order strings with text
            df = df.replace({
                'Q28|Q11|Q12|Q13':'Visibility ($\geq$2,1,0)',
                'Q28|Q13|Q12|Q11':'Invisibility (0,1,$\geq$2)'
                })
            
        
        # Name the remaining columns
        df = df.rename(columns=uv.get_variable_names())
        
        # Store cleaned-up dataframe
        dataDict[dtype][layout] = df.copy()
        
        # Make the columns multi-level
        columns = [(col, dtype, layout) for col in df.columns]
        columns = pd.MultiIndex.from_tuples(columns)
        df.columns = columns
        
        # Append to dataframe
        df_all = pd.concat([df_all,df],axis=1)
        
    # Sort index so top level variables are together in dataframe
    df = df_all.sort_index(axis=1)
        
    # Save the results dictionary and dataframe to pickle
    io.write_pickle('../data/refined/responses_dict', dataDict)
    io.write_pickle('../data/refined/responses_df', df)
    
    return dataDict, df


if __name__ == '__main__':
    dataDict, df = ingest_survey_data()
