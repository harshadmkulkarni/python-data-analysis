import pandas as pd
import matplotlib.pyplot as plt

#import our data file
stock_prices = pd.read_csv('intel_stock_price.csv')

#print DataFrame
print(stock_prices)
#create bar plot with xaxis=year and yaxis=life expectancy
stock_prices.plot(kind='bar',y='price')
#name the xaxis
plt.xlabel('Month')
#name the yaxis
plt.ylabel('Prices')
#show the plot
plt.show()
