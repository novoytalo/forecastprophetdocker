

# The model should be re-trained when new data becomes available. There is no point to re-train model, if data is not changed. Save model instead and use it again, when user wants to call predict function. Use pickle functionality for that:
from xml.dom.minidom import TypeInfo
from xml.etree.ElementTree import tostring
import pandas as pd
import csv
import json
import prophetNewPrevision2
from crypt import methods
import pickle
# from prophet import Prophet
# m = Prophet()
m = prophetNewPrevision2.calcProphet()
with open('forecast_model.pckl', 'wb') as fout:
    pickle.dump(m, fout)
with open('forecast_model.pckl', 'rb') as fin:
    m2 = pickle.load(fin)
    
 
#expose 3001
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
@app.route("/newdata", methods=['POST'])
def newdata():
    value=request.json
    print(value)

    
    # df=pd.DataFrame.from_dict(value)
    # df=pd.read_json(value)
    # value.to_csv('mod.csv')
    # df.to_csv('mod.csv')
    
    # df = pd.json_normalize(value['values'])
    # extract_data=value['tabledata']
    # data_file= open('csvs/mod.csv', 'w')
    # csv_writer=csv.writer(data_file)
    # count = 0
    # for data in value:
    #     if count == 0:
    #         header = data.keys()
    #         csv_writer.writerow(header)
    #         count += 1
    # csv_writer.writerow(data.values())
 
    # data_file.close()
    
    # value=value['tabledata']
    df = pd.json_normalize(value)
    df.to_csv('csvs/mod.csv')
    return value
    # print(request.json)
    # prophetNewPrevision.calcProphet()
@app.route("/katana-ml/api/v1.0/forecast/ironsteel", methods=['GET'])
def predict():
    # prophetNewPrevision.calcProphet()
    horizon = int(request.json['horizon'])
    
    future2 = m2.make_future_dataframe(periods=horizon)
    forecast2 = m2.predict(future2)
    
    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    
    ret = data.to_json(orient='records', date_format='iso')
    
    return ret
# running REST interface, port=3000 for direct test

    
if __name__ == "__main__":
    # debug True = hot heload = dev mode
    app.run(debug=True, host='0.0.0.0', port=3001)