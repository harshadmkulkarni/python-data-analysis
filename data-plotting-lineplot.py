import pandas as pd
import matplotlib.pyplot as plt

#import our data file
stock_prices = pd.read_csv('intel_amd_stock_prices.csv')

#print DataFrame
print(stock_prices)

#create y-columns
ycol = ['INTEL','AMD']
#create x-column
xcol =['Month']
#name and assign axis
stock_prices.plot()
#plot title
plt.title('Monthly Stock Prices for Top-2 Chip Manufacturers in the World')
#title for x-axis
plt.ylabel('PRICES ($USD)')
#show plot
plt.show()
