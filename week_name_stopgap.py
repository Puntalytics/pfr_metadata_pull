#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:11:02 2020

@author: dennisbrookner
"""

import pandas as pd

playoff_dict = {"Wild Card": 18,
                "Divisional": 19,
                "Conf Champ": 20,
                "Super Bowl": 21}

def fix_weeks(input_file, output_path):
    '''
    Input file should point to the csv created by pfr_meta_data_pull
    
    Output path should point to the desired location of the metadata, and should NOT have a trailing slash.

    This function fixes the fact that up until this point in the pipeline, "Week" is still
    a string, and needs to be parsed into an integer
    '''
    
    data = pd.read_csv(input_file)
    
    week_number= list(data['Week'])
    
    for i in range(len(week_number)):
        if "Week" in week_number[i]:
            week_number[i] = int(week_number[i].split('Week ')[1])
        elif week_number[i] in playoff_dict:
            week_number[i] = playoff_dict[week_number[i]]
        else:
            raise ValueError(f'Unexpected week name {week_number[i]}')
            
    data['Week_name'] = data['Week']
    
    data['Week'] = week_number
    
    data.to_csv(f'{output_path}/game_meta_data_weeks_fixed.csv')
    
    return

def main():
    print('Script was run directly, but this doesn\'t do anything!')
    
if __name__ == '__main__': main()
