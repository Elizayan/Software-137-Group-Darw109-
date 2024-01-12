import os
import pandas as pd
import glob
import numpy as np
from pandas import Series, DataFrame
glob.glob('data/CSV*.csv')
df1=pd.read_csv(r'D:\Studying\2023 ss\137 soft ware now\Assignment\Assignment 2/CSV1.csv',
                usecols=['SHORT-TEXT'])
df2=pd.read_csv(r'D:\Studying\2023 ss\137 soft ware now\Assignment\Assignment 2/CSV2.csv',
                usecols=['TEXT'])
df3=pd.read_csv(r'D:\Studying\2023 ss\137 soft ware now\Assignment\Assignment 2/CSV3.csv',
                usecols=['TEXT'])
df4=pd.read_csv(r'D:\Studying\2023 ss\137 soft ware now\Assignment\Assignment 2/CSV4.csv',
                usecols=['TEXT'])
all_dfs=[df1,df2,df3,df4]
len(all_dfs)
df=pd.concat(all_dfs)
df.to_csv(r'D:\Studying\2023 ss\137 soft ware now\Assignment\Assignment 2\LHJ.csv')

# In this part we try to firstly put this text in one csv. file
