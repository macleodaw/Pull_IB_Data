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
print(data_v2)

#replace empty celss with -
y = data_v2['Dividend_per_Share'].replace('-','0')
y2 = data_v2['EPS_Basic_from_Continued_Ops'].replace('-','0')
#convert string data to a float
y = y.astype('float')
y2 = y2.astype('float')

data_v2["payout_ratio"] = y/y2
print(data_v2)

#get the names
names=data_v2['EPIC']
#delete duplicates
names_group = names.drop_duplicates()

#new data frame for data
new_df = pd.DataFrame(columns=['EPIC', 'Mean Payout','Variance Payout'])

#loop to find average ratio
for names_single in names_group:
    #This says what we're searching by
    slice_by = 'EPIC'
    #from the loop set up it will go through all these single names
    variable_to_search2 = names_single
    #this extracts the data based on name
    company_for_stats = data_v2[data_v2[slice_by] == variable_to_search2]
    #these will look at the above data and calculate stats
    mean = statistics.mean(company_for_stats["payout_ratio"])
    variance = statistics.variance(company_for_stats["payout_ratio"])
    #creats a row to add to the data frame
    new_row = {'EPIC': names_single, 'Mean Payout': mean, 'Variance Payout': variance}
    #adds to data frame
    new_df = new_df.append(new_row, ignore_index=True)

print(new_df['EPIC'])

#if outlier remove it
new_df.drop(new_df[new_df['EPIC'] == '31/12/2015'].index, inplace = True)
data_v2.drop(data_v2[data_v2['EPIC'] == 'MRO'].index, inplace = True)

#set up the subplot
fig, axs = plt.subplots(3, 1, constrained_layout=True)
fig.suptitle( variable_to_search+ 'fundamental Analysis', fontsize=16)

axs[0].plot(data_v2['EPIC'],data_v2['payout_ratio'],'ro')
axs[0].set_title('Payout ratios individual')
axs[0].set_xlabel('EPIC')
axs[0].set_ylabel('Payout ratios')


axs[1].plot(new_df['EPIC'],new_df['Mean Payout'],'ro')
axs[1].set_title('Payout ratios 5 year average')
axs[1].set_xlabel('EPIC')
axs[1].set_ylabel('Payout ratios average')

axs[2].plot(new_df['EPIC'],new_df['Variance Payout'],'ro')
axs[2].set_title('Payout ratios variance')
axs[2].set_xlabel('EPIC')
axs[2].set_ylabel('Payout ratios variance')

plt.show()

