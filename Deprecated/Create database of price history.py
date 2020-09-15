import pandas as pd

data=[]
full_dataframe=[]
data = pd.read_csv (r'tickers.csv')
#create master dataframe
setup = pd.read_csv (r'ABF.csv')
full_dataframe=setup.loc[: , "Close"]
date=setup.loc[: , "DateTime"]

complete=[]
full=pd.concat([date], axis=1)
#put in the extra row for the ticker
full.loc[-1] = 'ticker'
full.index = full.index + 1  # shifting index
full = full.sort_index()  # sorting by index

#import tickers and then re-arrange
title = pd.read_csv (r'tickers.csv')
print(title)

count = 0
while (count <= 100):

    ticker = data.iloc[count, 0]
    print(ticker)
    price_data= pd.read_csv(ticker+'.csv')
    price_data=price_data.loc[: , "Close"]
    #add in the extra row for the ticker
    price_data.loc[-1] = title.loc[count,"EPIC"]
    price_data.index = price_data.index + 1  # shifting index
    price_data = price_data.sort_index()  # sorting by index
    full = pd.concat([full, price_data], axis=1)
    count = count + 1

print(full)
full.to_csv('FTSEPriceHistory.csv')