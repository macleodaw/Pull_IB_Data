import pandas as pd
from pandas import DataFrame

full_dataframe=[]
data = pd.read_csv(r'LSE_Financials_FTSE100.csv')
#print(data)

slice_by='Sector'
variable_to_search=' Industrials '

data=data[data[slice_by] == variable_to_search]

print(data)