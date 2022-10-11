import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import json
import sys
from collections import OrderedDict
from datetime import date

def calcProphet (value_json, periods):
    df=pd.DataFrame(value_json)
    # reorder collumns
    df = df[['Order_Date', 'Quantity']].dropna()
    #my data base data is on format dd/mm/yyyy
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
    print(df, file=sys.stderr)
    df = df.set_index('Order_Date')
    
    # daily_df = df.resample('D').mean()
    # print (daily_df, file=sys.stderr)
    # d_df = daily_df.reset_index().dropna()
    d_df = df.reset_index().dropna()
    d_df.columns = ['ds', 'y']
    size_data_json=len(d_df)
    # print (size_data_json, file=sys.stderr)
    # print (d_df, file=sys.stderr)
    # print (d_df, file=sys.stderr)
    # training

    m = Prophet()
    m.fit(d_df)
    # future = m.make_future_dataframe(periods=30)
    future = m.make_future_dataframe(periods)
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    # cut data to show only the futurecast ... not the fit
    fore= forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][size_data_json:]
    
    
    # print ('forecast after: '+ forecast , file=sys.stderr)
    # return forecast
    return fore
