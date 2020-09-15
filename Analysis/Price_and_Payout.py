import pandas as pd
import matplotlib.pyplot as plt
import os
import statistics

full_dataframe=[]
data = pd.read_csv(r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data\CSV database\LSE_Financials_FTSE100.csv')
#print(data)

#controls
slice_by='Sector'
variable_to_search=' Industrials '

#Create new folder for sector
#strip removes what's at the strat of the folder name
folder_name_sector=variable_to_search.strip()
sector_path = r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data'
sector_path=os.path.join(sector_path, '')+folder_name_sector
if not os.path.exists(sector_path):
    os.makedirs(sector_path)

#slicing the data, uncomment to slice
data_v2=data[data[slice_by] == variable_to_search]
#data_v2=data

#fundamental to look at
Fundamental='Dividend_per_Share'
Fundamental2='EPS_Basic_from_Continued_Ops'
Fundamental3='PE_Ratio'
Fundamental4='ROCE'
Fundamental5='EPS_Growth'

#fundamental to display
df_fund = pd.DataFrame({'Dividend_per_Share': [Fundamental], 'EPS_Basic_from_Continued_Ops': [Fundamental2], 'PE_Ratio': [Fundamental3], 'ROCE': [Fundamental4], 'EPS_Growth': [Fundamental5], 'payout_ratio': [Fundamental5]})

#append data onto data set for reduced set
data_v2=data_v2[['EPIC','Company_Name','Sector','SubSector','Financial_YE','Curreny',Fundamental,Fundamental2,Fundamental3,Fundamental4,Fundamental5]]


#takes the data and converst the fundamental data into float
y21 = data_v2['Dividend_per_Share'].replace('-','0')
y21 = y21.astype('float')
y22 = data_v2['EPS_Basic_from_Continued_Ops'].replace('-','0')
y22 = y22.astype('float')
y23 = data_v2['PE_Ratio'].replace('-','0')
y23 = y23.astype('float')
y24 = data_v2['ROCE'].replace('-','0')
y24 = y24.astype('float')
y25 = data_v2['EPS_Growth'].replace('-','0')
y25 = y25.astype('float')
#put it back into data frame
data_v2['Dividend_per_Share']=y21
data_v2['EPS_Basic_from_Continued_Ops']=y22
data_v2['PE_Ratio']=y23
data_v2['ROCE']=y24
data_v2['EPS_Growth']=y25

#replace empty celss with -
y = data_v2['Dividend_per_Share'].replace('-','0')
y2 = data_v2['EPS_Basic_from_Continued_Ops'].replace('-','0')
#convert string data to a float
y = y.astype('float')
y2 = y2.astype('float')

data_v2["payout_ratio"] = y/y2
#print(data_v2)

#extract the price info
price = pd.read_csv(r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data\CSV database\price.csv')
#get the names in the sliced subset
names=data_v2['EPIC']

#to get single names
#names=data_v2[data_v2['EPIC']=='AHT']

#delete duplicates and use this to loop
names_group = names.drop_duplicates()
#names_group='AHT'
#print(names_group)

#this sets up the new data frame to be populated
new_df = pd.DataFrame(columns=['EPIC', 'YE date','Price','Price date','Payout ratio','PE_Ratio','ROCE','EPS_Growth'])

#this will loop throught the indiviaul names in the selections and lopp creating names and dates for relevant ticker
for single_name in names_group:
    #for the single name make a smaller subset
    interested_data=data_v2[data_v2['EPIC'] == single_name]
    #subset the price info based ont the ticker of interest
    interested_price=price[price['EPIC'] == single_name]
    #reset the index so I can combine
    df1=interested_price.reset_index()
    #print(df1)
    df2=interested_data.reset_index()
    #print(df2)

    #This creates a new bigger data set
    df1['payout_ratio']=df2['payout_ratio']
    df2['Price']=df1['Price']
    df2['Price date']=df1['Price date']
    #print(df2)
    interested_price=df2

    ticker = single_name
    data = interested_price[interested_price['EPIC'] == ticker]
    print(data)

    #this will loop through each fundamental to print
    for fundamental in df_fund:
        print(data[fundamental])


        # create figure and axis objects with subplots()

        #controls the size
        fig, ax = plt.subplots(figsize=(10, 10))

        # make a plot
        ax.plot(data['Financial_YE'], data['Price'], color="red", marker="o", label="Price")
        # set x-axis label
        ax.set_xlabel("year", fontsize=14)
        # set y-axis label
        ax.set_ylabel("Price [p]", color="red", fontsize=14)

        # twin object for two different y-axis on the sample plot
        ax2 = ax.twinx()
        # make a plot with different y-axis using second axis object
        ax2.plot(data['Financial_YE'], data[fundamental], color="blue", marker="o", label="Payout")
        ax2.set_ylabel(fundamental, color="blue", fontsize=14)
        ax.set_title(fundamental+' and Price: ' + ticker, horizontalalignment='center', verticalalignment='top')

        # save analysis is folder

        sector_path = r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data'
        sector_path = os.path.join(sector_path, '') + folder_name_sector
        ticker_path = os.path.join(sector_path, '') + single_name
        if not os.path.exists(ticker_path):
            os.makedirs(ticker_path)

        plt.savefig(os.path.join(ticker_path, '') + fundamental +' vs price ' + ticker + '.png')
        print(os.path.join(ticker_path, '') + fundamental +'payout ratio vs price ' + ticker + '.png')

        #plt.show()
        #plt.pause(3)
        plt.close()








