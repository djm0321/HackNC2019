# Import yfinance
import yfinance as yf
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('MMM','2016-01-01','2017-01-01')

# Plot the close prices
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
print(type(data))
#print(data['Date'])
#pd.to_datetime(data['Date'],format='%m/%d/%Y')

#data = data.set_index(pd.datetimeIndex(data['Date']))

sns.lineplot(x=data.index, y="Close", data=data);
plt.show()
#pd.to_datetime(df['DATES'],format='%m/%d/%Y')
