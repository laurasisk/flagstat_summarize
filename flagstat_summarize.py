#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:26:00 2025

@author: Laura Sisk-Hackworth
"""

import pandas as pd
import os

#folder_name = sys.argv[1]

#List 
input_dir = os.getcwd()
files = [f for f in os.listdir(input_dir) if f.endswith('.tsv')]


print('File list:')
print(files)

files_small_test = files[0:2]


##add files to dictionary
file_dictionary = {}

#loop through files
for file in files: 
     #open the file and save as a data frame
     file_df = pd.read_csv(file, header=None, sep='\t')
     
     # remove percent sign characters
     file_df = file_df.replace('%', '', regex=True)
     # replace spaces with underscore
     file_df = file_df.replace(' ', '_', regex=True)
     #Make the index names the third column 
     file_df.set_index(file_df.columns[2], inplace=True)
     #remove the second column, which is just zeroes, and the third column which has been converted to the index
     file_df.drop(file_df.columns[1:2], axis=1, inplace=True)
     #make the data in the frame numeric
     file_df[0] = pd.to_numeric(file_df[0], downcast='float', errors='coerce')
     #print file name and the data for viewer
     print(file)
     print(file_df)
     #add the data frames to a dictionary, with key as sample name
     file_dictionary[file.split('_', 1)[0]] = file_df
     print('processed')
     
##make data frame of all sample values
combo_df = pd.concat(file_dictionary.values(), axis = 1, keys = file_dictionary.keys())
combo_df.head()

#calculate means for each row
combo_df_mean = combo_df.copy()
combo_df_mean['average'] = combo_df.mean(axis=1)

#to csv
combo_df_mean.to_csv('flagstat_results_summary.csv')
