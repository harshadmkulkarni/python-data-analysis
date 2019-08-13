import pandas as pd
import matplotlib.pyplot as plt
#import our data file
lifeexp = pd.read_csv('irish_life_expec.csv')

#create scatter plot with xaxis=year and yaxis=life expectancy
lifeexp.plot(kind='scatter', x='year', y='life expec')
#plot title
plt.title('Irish Life Expectancy')
#add x-axis label
plt.xlabel('Age')
#add y-axis label
plt.ylabel('Life Expectancy')
#show plot
plt.show()
