import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
import json
import sys
from collections import OrderedDict
from datetime import date
def calcProphet (value_json):
    df=pd.DataFrame(value_json)
    # reorder collumns
    df = df[['Order_Date', 'Quantity']].dropna()
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df = df.set_index('Order_Date')
    daily_df = df.resample('D').mean()
    d_df = daily_df.reset_index().dropna()
    d_df.columns = ['ds', 'y']

    # training

    m = Prophet()
    m.fit(d_df)
    future = m.make_future_dataframe(periods=10)
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-90:]
    
    return forecast
