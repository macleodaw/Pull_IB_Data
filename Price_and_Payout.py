import pandas as pd
import matplotlib.pyplot as plt
import statistics

full_dataframe=[]
data = pd.read_csv(r'LSE_Financials_FTSE100.csv')
#print(data)

#controls
slice_by='Sector'
variable_to_search=' Industrials '

#slicing the data, uncomment to slice
data_v2=data[data[slice_by] == variable_to_search]
#data_v2=data

#fundamental to look at
Fundamental='Dividend_per_Share'
print(data_v2.keys())
Fundamental2='EPS_Basic_from_Continued_Ops'

#append data onto data set for reduced set
data_v2=data_v2[['EPIC','Company_Name','Sector','SubSector','Financial_YE','Curreny',Fundamental,Fundamental2]]

#replace empty celss with -
y = data_v2['Dividend_per_Share'].replace('-','0')
y2 = data_v2['EPS_Basic_from_Continued_Ops'].replace('-','0')
#convert string data to a float
y = y.astype('float')
y2 = y2.astype('float')

data_v2["payout_ratio"] = y/y2
print(data_v2)

#extract the price info
price = pd.read_csv(r'price.csv')
print(price)
#get the names in the sliced subset
names=data_v2['EPIC']
#delete duplicates and use this to loop
names_group = names.drop_duplicates()

#this sets up the new data frame to be populated
new_df = pd.DataFrame(columns=['EPIC', 'YE date','Price','Price date','Payout ratio'])

#this will loop throught the indiviaul names in the selections and lopp creating names and dates for relevant ticker
for single_name in names_group:
    #for the single name make a smaller subset
    interested_data=data_v2[data_v2['EPIC'] == single_name]
    #subset the price info based ont the ticker of interest
    interested_price=price[price['EPIC'] == single_name]
    #pd.Series(np.random.randn(sLength), index=df1.index)
    interested_price['payout_ratio']=interested_data.iloc[:, 8].values

#select the ticker of interst
ticker='SPX'
data=interested_price[interested_price['EPIC'] == ticker]


# create figure and axis objects with subplots()
fig,ax = plt.subplots()
# make a plot
ax.plot(data['YE date'], data['Price'], color="red", marker="o",label="Price")
# set x-axis label
ax.set_xlabel("year",fontsize=14)
# set y-axis label
ax.set_ylabel("Price [p]",color="red",fontsize=14)

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(data['YE date'], data['payout_ratio'],color="blue",marker="o",label="Payout")
ax2.set_ylabel("Payout_ratio",color="blue",fontsize=14)
ax.set_title('Payout Ratio and Price: ' + ticker, horizontalalignment='center', verticalalignment='top')

plt.show()
