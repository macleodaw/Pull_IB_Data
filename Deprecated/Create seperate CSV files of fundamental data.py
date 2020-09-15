import pandas as pd
from pandas import DataFrame

data = pd.read_csv (r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data\CSV database\LSE_Financials_FTSE100.csv')

headers=list(data)
headers = DataFrame(headers)
print(headers)

EPIC = data.loc[:,"EPIC"]
Name = data.loc[:,"Company_Name"]
FinancialYE = data.loc[:,"Financial_YE"]
Currency=data.loc[:,"Curreny"]
Base=pd.concat([EPIC, Name,FinancialYE,Currency], axis=1)

count = 6
while (count < (headers.shape[0]-1)): #headers.shape[0]):
    count = count + 1
    print(count)
    title = headers.iloc[count,0]
    print(title)
    floating_data=data.loc[:,title]
    print(floating_data)
    full = pd.concat([Base, floating_data], axis=1)
    print(full)
    #df= pandas.to_datetime(full)
    full.to_csv(title +'.csv')