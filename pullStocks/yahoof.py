# Import yfinance
import yfinance as yf
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
def getStock(stock,start,end):
    data = yf.download(stock,start,end)
    sns.set_style("darkgrid")
    plt.style.use('dark_background')

    plt.margins(x=0.01,y=0.01)
    sns.lineplot(x=data.index, y="Close", data=data,color = "lightgreen",lw=2)#make graph
    plt.ylabel("Value($)")
    plt.title(stock + " from " + start + " to " + end)
    plt.show()

getStock("MMM",'2016-01-01','2017-01-01')
