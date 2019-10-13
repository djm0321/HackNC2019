# Import yfinance
import yfinance as yf
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
def getStock(stock,start,end):
    df = pd.read_csv('companies.csv',engine='python')
    data = yf.download(df.iloc[stock,0],start,end)
    sns.set_style("darkgrid")
    plt.style.use('dark_background')

    plt.margins(x=0)
    sns.lineplot(x=data.index, y="Close", data=data,color = "lightgreen",lw=2)#make graph
    plt.ylabel("Value($)")
    plt.title(df.iloc[stock,1] + " from " + start + " to " + end)
    plt.show()


getStock(100,'2010-01-01','2019-01-01')
