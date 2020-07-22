import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

full_dataframe=[]
data = pd.read_csv(r'LSE_Financials_FTSE100.csv')

#controls
slice_by='Sector'
variable_to_search=' Industrials '
Fundamental='Dividend_per_Share'

#slicing the data
data=data[data[slice_by] == variable_to_search]
data=data[['EPIC','Company_Name','Sector','SubSector','Financial_YE','Curreny',Fundamental]]

#print(data)
dps=data[[Fundamental]]

x_axis=list(range(0, 50))
y_axis=list(range(1, 85))

new_list = []
count = 0
print(len(dps))

while (count <= 10):
    dps_ind=(dps.iloc[count,0])
    if dps_ind == "-":
        dps_ind=0
    dps_ind = float(dps_ind)
    new_list.append(dps)
    count=count+1

print(new_list)
print(len(new_list))
#plt.scatter(x_axis,new_list)
#plt.show()

