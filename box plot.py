# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:44:10 2021

@author: Michael
"""

#Purpose: Create box plot for period 2 data
#Name: Michael Moyneur
#Date: 10/11/21
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata2.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()