#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

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
    if req.get("result").get("action") != "room.availability":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("RoomType")

    availability = {'Desk':'Available', 'Conference Room 27NA':'Available', 'Conference Room 27S':'Available', 'Room 27C45':'Available', 'Room 27C47':'Available', 'Room 27A22':'Available', 'Room 27B13':'Available'}

    speech = "Rooms available are " + zone + " is " + str(availability[zone]) + "."

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-EchoProject-Availability"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
