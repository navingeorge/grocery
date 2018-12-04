
    #!/usr/bin/env python
import urllib
import json
import os
from flask import Flask
from flask import request
from flask import make_response
import pandas as pd
import pymysql

conn = pymysql.connect(host="localhost", user = "root", password = "python",db="grocery")
print("Opened database successfully")
sql=("SELECT * FROM grocery;")
pan = pd.read_sql(sql, conn)
print(pan)
pd1 = pd.DataFrame(pan)
c1 = pd1['PRODUCT'].tolist()

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
def makeWebhookResult(req):
    # if req.get("queryResult").get("action") != "price":
    #     return {}
    result = req.get("queryResult")
    print(req.get("queryResult").get("action"))
    parameters = result.get('parameters')
    
    m=req.get("queryResult").get("action")
   
    if(req.get("queryResult").get("action") == "price"):
     c2 = pd1['COST'].tolist()
    elif(req.get("queryResult").get("action") == "quantity"):
     c2 = pd1['QUANTITY'].tolist()
     
    elif(req.get("queryResult").get("action") == "exp"):
     c2 = pd1['EXPDATE'].tolist()
     
  
    zone = parameters.get("Product")
    cost = dict(zip(c1,c2))
    print(cost)
    speech = req.get("queryResult").get("action") +" of "+ zone + " is " + str(cost[zone])
    print("Response:")
    print(speech)
    return {
        "fulfillmentText": speech,
        "fulfillmentMessages":[
         {
          "text": {
           "text": [speech]
          }
         }
        ],
        #"data": {},
        #"contextOut": [],
        "source": "My_chatbot"
    }
if __name__ == '__main__':
    port = int(os.getenv('PORT', 79))
    print ("Starting app on port %d" %(port))
    app.run(debug=True, port=port, host='0.0.0.0')


