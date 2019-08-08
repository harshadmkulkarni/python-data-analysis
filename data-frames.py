import numpy as np
import pandas as pd
####################### DATAFRAME from ARRAY ###############################
#creates an array of elements 24-34 and displays them in 2rows x 5cols
#array1 = np.arange(24,34).reshape(2,5)
#print (array1)

#creates a dataframe from array1 and renames default row & columns header labels
#df = pd.DataFrame(data=array1, columns=['COL-1','COL-2','COL-3','COL-4','COL-5'])
#print(df)

###################### DATAFRAME from DICTIONARY #############################

#Dictionary is key-value pair datastructure
course_sales = {'course-name':['Python','AI','Machine Learning','Data Science'],
                'class-day':['Mon','Tue','Wed','Thu'],
                'orig-price':['$2000','$10000','$5000','$6000'],
                'sale-price':['$1500','$6600','$3500','$3900']
                }
#print(course_sales)

#DataFrame from Dictionary
df_course_sales = pd.DataFrame(course_sales)
#print(df_course_sales)

###################### LISTS to DICTIONARY to DATAFRAME #########################
courses =['Python','AI','Machine Learning','Data Science']
days = ['Mon','Tue','Wed','Thu']
origprices = ['$2000','$10000','$5000','$6000']
saleprices = ['$1500','$6600','$3500','$3900']
cols = [courses, days, origprices, saleprices]
labels = ['COURSE_NAME', 'DAYS_OF_CLASS', 'ORIG_PRICE', 'SALE_PRICE']

master_list=list(zip(labels,cols))
#print(master_list)

data=dict(master_list)
df_new_course_sales=pd.DataFrame(data)
print(df_new_course_sales)

### DATAFRAME BROADCASTING is feature of NumPy & a great technique to quick-update new/existing column data ###
df_new_course_sales['AUG_SALE_PRICE']='$1000'
df_new_course_sales['SEP_SALE_PRICE']='$900'
print(df_new_course_sales)

#rename column labels for dataframe
labels = ['COURSE_NAME', 'DAYS_OF_CLASS', 'ORIG_PRICE', '24HR_PRICE', '48HR_PRICE', '72HR_PRICE']
df_new_course_sales.columns = labels
print(df_new_course_sales)
