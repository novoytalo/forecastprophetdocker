from neuralprophet import NeuralProphet
import pandas as pd
import sys

def neuralProphetCal(value_json,periods):
    df=pd.DataFrame(value_json)
    
    # reorder collumns
    df = df[['Order_Date', 'Quantity']].dropna()
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
    
    df = df.set_index('Order_Date')
    # print('inside')
    # print(df, file=sys.stderr)
    d_df = df.reset_index().dropna()
    d_df.columns = ['ds', 'y']
    size_data_json=len(d_df)
    
    # print(d_df, file=sys.stderr)
    #### original
    # df = pd.read_csv('Dow Jones Iron & Steel Historical Data.csv')
    # print(df, file=sys.stderr)
    m = NeuralProphet()
    print (d_df, file=sys.stderr)
    # future = m.make_future_dataframe(periods)
    # metrics = m.fit(df, freq="D")
    metrics = m.fit(d_df)
    # future = m.make_future_dataframe(periods)
    
    forecast = m.predict(d_df)
    print ('5OOOooooooooooo: ', file=sys.stderr)
    return forecast