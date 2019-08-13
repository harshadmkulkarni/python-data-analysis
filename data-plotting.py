# Plotting with Pandas
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('intel.csv', index_col='Date', parse_dates=True)
#print (df.info())
print(df.head())

#close_value = df['Close'].values
#print(type(close_value))

# create first Plot with NumPy
# plt.plot(close_value)
# show first Plot with NumPy
# plt.show()

#create first Plot with DataFrame
#df.plot()
#plt.show()

#create specified plot with color green and with a legend
#df['Close'].plot(color='g', style='-', legend=True)
#plt.axis(('2017','2018',0,60))
#plt.show()

#how to plot data
df.plot(color='blue')
plt.title('Stock Prices')
plt.xlabel('Date Range')
plt.ylabel('Price ($)')
plt.show()
#save and export the plotted data to files
plt.savefig("df.png")
