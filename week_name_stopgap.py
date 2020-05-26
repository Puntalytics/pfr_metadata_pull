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

data = pd.read_csv('data/game_meta_data.csv')

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

data.to_csv('data/game_meta_data_weeks_fixed.csv')
