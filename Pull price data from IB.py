import pandas as pd
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time
# Working with Pandas DataFrames
import pandas
#import the csv file with all the ticker information
data=[]
data = pd.read_csv (r'tickers.csv')







class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def historicalData(self, reqId, bar):
        print(f'Time: {bar.date} Close: {bar.close}')
        app.data.append([bar.date, bar.close])


def run_loop():
    app.run()


app = IBapi()
app.connect('127.0.0.1', 7497, 123)

# Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1)  # Sleep interval to allow time for connection to server

# Create contract object
#Create contract object

#establish loops
count = 0
while (count < 1):

    ticker = data.iloc[count, 0]
    eurusd_contract = Contract()
    eurusd_contract.symbol = ticker
    eurusd_contract.secType = 'STK'
    eurusd_contract.exchange = 'LSE'
    eurusd_contract.currency = 'GBP'
    app.data = []  # Initialize variable to store candle

    # Request historical candles
    app.reqHistoricalData(1, eurusd_contract, '', '6 Y', '1 day', 'BID', 0, 2, False, [])

    time.sleep(5)  # sleep to allow enough time for data to be returned

    df = pandas.DataFrame(app.data, columns=['DateTime', 'Close'])
    df['DateTime'] = pandas.to_datetime(df['DateTime'])
    df.to_csv(ticker+'.csv')

    print(df)
    count = count + 1

app.disconnect()