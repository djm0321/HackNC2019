# Import yfinance
import yfinance as yf

# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('MMM','2016-01-01','2017-01-01')
print(type(data))
# Plot the close prices
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#print(data)

plot = sns.relplot(x="Date", y="Close", data=data);
#plot.show()
