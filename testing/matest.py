from __future__ import division

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
from pandas.io.data import DataReader
from datetime import datetime

tech_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

end = datetime.now()

start = datetime(end.year - 1, end.month, end.day)

for stock in tech_list:
    globals()[stock] = DataReader(stock,'yahoo',start,end) 
    

#AAPL['Adj Close'].plot(legend=True,figsize=(10,4))

ma_day = [10,20,50]

for ma in ma_day:
    column_name = "MA %s" %(str(ma))

    AAPL[column_name] = pd.rolling_mean(AAPL['Adj Close'],ma)

#AAPL[['Adj Close', 'MA 10', 'MA 20', 'MA 50']].plot(subplots=False,figsize=(10,4))

AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()

#AAPL['Daily Return'].plot(figsize=(10,4),legend=True,linestyle='--',marker='o')

sns.distplot(AAPL['Daily Return'].dropna(),bins=100,color = 'purple')

#AAPL['Volume'].plot(legend=True,figsize=(10,4))
plt.show()
