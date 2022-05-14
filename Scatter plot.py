# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:04:37 2021

@author: Michael
"""

#Purpose: Create scatter plot of humidity for period 1. Can replace df1 to df2 to display second period data
#Name: Michael Moyneur
#Date: 10/11/21
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
plt.scatter(df1.index.values,df1['Humidity']); plt.suptitle('Humidity')
plt.show()