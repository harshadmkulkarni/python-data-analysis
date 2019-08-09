import pandas as pd
import xlsxwriter

filepath = ('edited_googleplaystore_dataset.csv')

#create DataFrame df and read csv from filepath var
#df = pd.read_csv(filepath)
#display head contents of df
#print(df.head())

#create column names for edited_googleplaystore_dataset
column_names = ['App','Rating','Reviews','Size','Number of installs', 'Type','Price','Last Updated']

#create DataFrame df and read csv from filepath var
#na_values parameter replaces -1 with NaN value i.e (Not a Number)
df = pd.read_csv(filepath,header=None, names=column_names, na_values='-1')

#print dataset details within df DataFrame
#print(df.info())

#print full dataset in df
#print(df)

#display head contents of df i.e first 5 rows of dataset
#print(df.head())
#display tail contents of df i.e. last 5 rows of dataset
#print(df.tail())

#create an index column with Last Updated column for df
df.index = df['Last Updated']

#only prints specified columns in df with new index column above
new_columns = ['App','Reviews']
df=df[new_columns]

print(df)

#create a new csv file & export our cleaned data created in df above
#cleaned_csv_file = 'cleaned-google-playstore-data.csv'
#df.to_csv(cleaned_csv_file)

#create a new excel file & export our cleaned data created in df above
cleaned_excel_file = 'cleaned-google-playstore-data-excel.xlsx'
df.to_excel (cleaned_excel_file)
