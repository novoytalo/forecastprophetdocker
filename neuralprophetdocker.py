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
    
    m = NeuralProphet()
    print (d_df, file=sys.stderr)

    # metrics = m.fit(df, freq="D")
    # metrics = m.fit(d_df, freq="D", epochs=1000)
    metrics = m.fit(d_df, freq= "D")
    
    future=m.make_future_dataframe(d_df,periods=periods)
    forecast=m.predict(future)
    print(forecast, file=sys.stderr)
  
    
    # forecast = m.predict(d_df)
    # print ('5OOOooooooooooo: ', file=sys.stderr)
    return forecast