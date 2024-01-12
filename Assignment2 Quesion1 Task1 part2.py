import pandas as pd
import os
import csv
csv_file=open(r'D:\学习\2023 ss\137 soft ware now\Assignment\Assignment 2/LHJ.csv', 'r')
csv_reader=csv.reader(csv_file)
txt_file=open('new_TEXT','w')
for row in csv_reader:
    txt_file.write('\t'.join(row)+'\n')
csv_file.close()
txt_file.close()

#then we set up a txt. file for the combination of that csv file