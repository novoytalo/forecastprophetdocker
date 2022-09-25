import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet


def calcProphet ():
    # df2=pd.read_csv('mod.csv')
    df = pd.read_csv('Dow Jones Iron & Steel Historical Data.csv')
    df = df[['Date', 'Price']].dropna()
    # df2 = df2[['Order_Date','Quantity']].dropna() 
    # print('creatAt and id ')
    # print (df2)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    daily_df = df.resample('D').mean()
    d_df = daily_df.reset_index().dropna()

    d_df.columns = ['ds', 'y']
    # fig = plt.figure(facecolor='w', figsize=(20, 6))
    # plt.plot(d_df.ds, d_df.y)

    # training

    m = Prophet()
    m.fit(d_df)
    future = m.make_future_dataframe(periods=90)
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    # forecast 90 days
    from datetime import datetime, timedelta
    fig1 = m.plot(forecast)
    #datenow = datetime.now()
    datenow = datetime(2019, 7, 2)
    dateend = datenow + timedelta(days=90)
    datestart = dateend - timedelta(days=450)
    plt.xlim([datestart, dateend])
    plt.title("Iron/steel forecast", fontsize=20)
    plt.xlabel("Day", fontsize=20)
    plt.ylabel("Iron/steel price", fontsize=20)
    plt.axvline(datenow, color="k", linestyle=":")
    plt.show()


    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-90:]

    #  show trends plot
    fig2 = m.plot_components(forecast)
    return m
    #cross validation, showing errors esperados 

    # from prophet.diagnostics import cross_validation, performance_metrics
    # df_cv = cross_validation(m, horizon='90 days')
    # df_p = performance_metrics(df_cv)
    # df_p.head(5)

    #show performance

    # from prophet.plot import plot_cross_validation_metric
    # fig3 = plot_cross_validation_metric(df_cv, metric='mape')
