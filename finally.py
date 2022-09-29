from xml.dom.minidom import TypeInfo
from xml.etree.ElementTree import tostring
import pandas as pd
import prophetNewPrevision
import prophetNewPrevision2
from crypt import methods
import sys
import pickle
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import logging
logging.getLogger('fbprophet').setLevel(logging.WARNING) 
# this call is only executed one time. Cause need to use the endpoint '/forecast_like_katana-ml'
# if you need to use only json this endpoint can be deleted. No problems.
# but all the time you need to retraining/fit
m = prophetNewPrevision.calcProphet()
print('FLASK CHANGED', file=sys.stderr)
app = Flask(__name__)
CORS(app)
@app.route("/newdata", methods=['POST'])
def newdata():
    value=request.json
    df = pd.json_normalize(value)
    df.to_csv('csvs/mod.csv')
    return value
@app.route("/forecast_json", methods=['GET'])
def predict():
    json_in = request.json
    # print (request.json, file=sys.stderr)
    try:
        forecast_result = prophetNewPrevision2.calcProphet(json_in)
        # print (forecast_result, file=sys.stderr)
        json_transformation= forecast_result.to_json(orient='records', date_format='iso')
    except:
        json_transformation= []
    # print(json_transformation, file=sys.stderr)
    return json_transformation
@app.route("/forecast_like_katana-ml", methods=['GET'])
#forecast using archive .csv ... like the exemple base. Don't need fit again the data
def predictUsingArchives():
    horizon = int(request.json['horizon'])
        
    with open('forecast_model.pckl', 'wb') as fout:
        pickle.dump(m, fout)
    with open('forecast_model.pckl', 'rb') as fin:
        m2 = pickle.load(fin)
    horizon = int(request.json['horizon'])
    
    future2 = m2.make_future_dataframe(periods=horizon)
    forecast2 = m2.predict(future2)
    
    data = forecast2[['ds', 'yhat', 'yhat_lower', 'yhat_upper']][-horizon:]
    
    ret = data.to_json(orient='records', date_format='iso')
    
    return ret

if __name__ == "__main__":
    # from waitress import serve
    # debug True = hot heload = dev mode
    #production server using Waitress
    # serve(app, host="0.0.0.0", port=3001)
    #debug develop server
    app.run(debug=True, host='0.0.0.0', port=3001)