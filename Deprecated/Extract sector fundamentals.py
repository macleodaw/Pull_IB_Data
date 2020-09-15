import pandas as pd
import matplotlib.pyplot as plt


full_dataframe=[]
data = pd.read_csv(r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data\CSV database\LSE_Financials_FTSE100.csv')
print(data)

#controls
slice_by='Sector'
variable_to_search=' Industrials '

#slicing the data, uncomment to slice
data_v2=data[data[slice_by] == variable_to_search]
#data_v2=data

#fundamental to look at
Fundamental='Dividend_per_Share'

#append data onto data set for reduced set
data_v2=data_v2[['EPIC','Company_Name','Sector','SubSector','Financial_YE','Curreny',Fundamental]]
print(data_v2)


#extract data for the date specified
data_v3=data_v2
#data_v3=data_v2[data_v2['Financial_YE'] == '31/12/2019']
print(data_v3)

#replace empty celss with -
y = data_v3['Dividend_per_Share'].replace('-','0')

#convert string data to a float
y = y.astype('float')

#plot the graph
plt.plot(data_v3['Company_Name'],y,'ro')
plt.xticks(rotation=90)
plt.show()

#get some stats
print(data_v3['Dividend_per_Share'].describe())

