### Just a Copy from the original post code, show that Docker cam be used white Prophet
### 

from xml.dom.minidom import TypeInfo
from xml.etree.ElementTree import tostring
from matplotlib import pyplot as plt
import pandas as pd
from crypt import methods
import sys
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

print('FLASK ORING', file=sys.stderr)

df = pd.read_csv('Dow Jones Iron & Steel Historical Data.csv')
df = df[['Date', 'Price']].dropna()
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
daily_df = df.resample('D').mean()
d_df = daily_df.reset_index().dropna()

d_df.columns = ['ds', 'y']
# fig = plt.figure(facecolor='w', figsize=(20, 6))
# plt.plot(d_df.ds, d_df.y)


m = Prophet()
m.fit(d_df)
future = m.make_future_dataframe(periods=90)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


from datetime import datetime, timedelta
# fig1 = m.plot(forecast)
datenow = datetime.now()
datenow = datetime(2019, 7, 2)
dateend = datenow + timedelta(days=90)
datestart = dateend - timedelta(days=450)
# plt.xlim([datestart, dateend])
# plt.title("Iron/steel forecast", fontsize=20)
# plt.xlabel("Day", fontsize=20)
# plt.ylabel("Iron/steel price", fontsize=20)
# plt.axvline(datenow, color="k", linestyle=":")
# plt.show()


forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-90:]

# fig2 = m.plot_components(forecast)

# from fbprophet.diagnostics import cross_validation, performance_metrics
# df_cv = cross_validation(m, horizon='90 days')
# df_p = performance_metrics(df_cv)
# df_p.head(5)


# from fbprophet.plot import plot_cross_validation_metric
# fig3 = plot_cross_validation_metric(df_cv, metric='mape')

import pickle
with open('forecast_model.pckl', 'wb') as fout:
    pickle.dump(m, fout)
with open('forecast_model.pckl', 'rb') as fin:
    m2 = pickle.load(fin)


from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
@app.route("/katana-ml/api/v1.0/forecast/ironsteel", methods=['POST'])
def predict():
    horizon = int(request.json['horizon'])
    
    future2 = m2.make_future_dataframe(periods=horizon)
    forecast2 = m2.predict(future2)
    
    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    
    ret = data.to_json(orient='records', date_format='iso')
    
    return ret
# running REST interface, port=3000 for direct test
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3001)