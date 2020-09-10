import pandas as pd

#load data
data = pd.read_csv(r'LSE_Financials_FTSE100.csv')
price=pd.read_csv(r'C:\Users\Allan W MacLeod\PycharmProjects\Pull_IB_Data\FTSEPriceHistory.csv')

#controls to search data
#problem sectors
slice_by='Sector'
variable_to_search=' Technology '

#slicing the data, uncomment to slice
#data_v2=data[data[slice_by] == variable_to_search]
data_v2=data
#fundamental to look at
Fundamental='Dividend_per_Share'
Fundamental2='EPS_Basic_from_Continued_Ops'

#append data onto data set for reduced set
data_v2=data_v2[['EPIC','Company_Name','Sector','SubSector','Financial_YE','Curreny',Fundamental,Fundamental2]]

#get the names in the sliced subset
names=data_v2['EPIC']
#delete duplicates and use this to loop
names_group = names.drop_duplicates()

#this sets up the new data frame to be populated
new_df = pd.DataFrame(columns=['EPIC', 'YE date','Price','Price date'])



#this will loop throught the indiviaul names in the selections and lopp creating names and dates for relevant ticker
for single_name in names_group:
    #for the single name make a smaller subset
    intereste_data=data_v2[data_v2['EPIC'] == single_name]
    intereste_dates=intereste_data['Financial_YE']
    #subset the price info based ont the ticker of interest
    interested_price=price[['date',single_name]]

    for dates_single in intereste_dates:
        # This says what we're searching by
        slice_by = 'date'
        # from the loop set up it will go through all these single names
        variable_to_search2 = dates_single

        # this extracts the data based on name
        print(single_name)
        print('first data')
        print(variable_to_search2)
        price_at_YE = interested_price[interested_price[slice_by] == variable_to_search2]

        # this checks for empty, likley if it falls on the weekedn and then moves back two days
        new_date=dates_single
        if price_at_YE.empty:
            # converts the missing entry
            day = int(str(variable_to_search2)[:2])
            month = int(str(variable_to_search2)[3:5])
            year = int(str(variable_to_search2)[6:10])
            # moves the day back two days so it's a weekday with prices
            new_day = day - 1
            if month < 10:
                print('for month')
                month='0' + str(month)
                print(month)
            if new_day < 10:
                print('for day')
                new_day ='0' + str(new_day)

            new_date = (str(new_day) + '/' + str(month) + '/' + str(year))

            variable_to_search3 = new_date
            print('second date')
            print(variable_to_search3)
            price_at_YE = interested_price[interested_price[slice_by] == variable_to_search3]
            # this checks if still empty, likley if it falls on the weekend and then moves back 3
            if price_at_YE.empty:
                new_day = day - 2
                if new_day < 1:
                    new_day = day + 2
                # adds in leading zero if it's missing for the month
                month=int(month)
                new_day=int(new_day)
                print(month)
                if month < 10:
                    month = '0' + str(month)
                if new_day < 10:
                    new_day = '0' + str(new_day)

                new_date = (str(new_day) + '/' + str(month) + '/' + str(year))

            variable_to_search4 = new_date
            print('third date')
            print(variable_to_search4)

            price_at_YE = interested_price[interested_price[slice_by] == variable_to_search4]

            #loop again for anotherinteration
            if price_at_YE.empty:
                new_day = day - 3
                if new_day < 1:
                    new_day = day + 3
                # adds in leading zero if it's missing for the month
                month=int(month)
                new_day=int(new_day)
                print(month)
                if month < 10:
                    month = '0' + str(month)
                if new_day < 10:
                    new_day = '0' + str(new_day)

                new_date = (str(new_day) + '/' + str(month) + '/' + str(year))

            variable_to_search5 = new_date
            print('fourth date')
            print(variable_to_search5)
            #print(price_at_YE)
            price_at_YE = interested_price[interested_price[slice_by] == variable_to_search5]

        # extract the price data
        price_at_YE = price_at_YE.iloc[0, 1]

        # creats a row to add to the data frame
        new_row = {'EPIC': single_name, 'YE date': dates_single, 'Price': price_at_YE, 'Price date':new_date}
        # adds to data frame
        new_df = new_df.append(new_row, ignore_index=True)

print(new_df)
new_df.to_csv( variable_to_search+' price.csv')
#new_df.to_csv('All price.csv')

#keep this code as a way to investigate if something is funny with ticker e.g. missing data
ticker='HLMA'
AHT=data_v2[data_v2['EPIC'] == ticker]
AHT_date=AHT['Financial_YE']

#makes data set to for price
AHT_price=price[['date',ticker]]

#new data set to store info
new_df1 = pd.DataFrame(columns=['EPIC', 'YE date','Price','Price date'])

for dates_single in AHT_date:
    #This says what we're searching by
    slice_by = 'date'
    #from the loop set up it will go through all these single names
    variable_to_search2 = dates_single

    #this extracts the data based on name
    price_at_YE = AHT_price[AHT_price[slice_by] == variable_to_search2]
    #this checks for empty, likley if it falls on the week and then moves back two days
    if price_at_YE.empty:
        #converts the missing entry
        day=int(str(variable_to_search2)[:2])
        month=int(str(variable_to_search2)[3:5])
        year=int(str(variable_to_search2)[6:10])
        #moves the day back two days so it's a weekday with prices
        new_day=day-2
        if new_day < 1:
            new_day = day + 2
        #adds in leading zero if it's missing for the month
        if month<10:
            new_date = (str(new_day) + '/0' + str(month) + '/' + str(year))
        else:
            new_date = (str(new_day) + '/' + str(month) + '/' + str(year))
        if new_day<10:
            new_date = '0' + (str(new_day) + '/' + str(month) + '/' + str(year))
        #use the new date to search the prices info
        variable_to_search3 = new_date
        #print(new_date)
        price_at_YE = AHT_price[AHT_price[slice_by] == variable_to_search3]
        if price_at_YE.empty:
            new_day = day - 3
            if new_day < 1:
                new_day = day + 3
            # adds in leading zero if it's missing for the month
            if month < 10:
                new_date = (str(new_day) + '/0' + str(month) + '/' + str(year))
            else:
                new_date = (str(new_day) + '/' + str(month) + '/' + str(year))
            if new_day < 10:
                new_date = '0' + (str(new_day) + '/0' + str(month) + '/' + str(year))
            # use the new date to search the prices info
            variable_to_search3 = new_date

            price_at_YE = AHT_price[AHT_price[slice_by] == variable_to_search3]


    #extract the price data
    price_at_YE=price_at_YE.iloc[0,1]
    #creats a row to add to the data frame
    new_row1 = {'EPIC': ticker, 'YE date': dates_single, 'Price': price_at_YE, 'Price date':new_date}
    #adds to data frame
    new_df1 = new_df1.append(new_row1, ignore_index=True)

