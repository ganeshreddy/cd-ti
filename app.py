#!/usr/bin/env python

import urllib
import json
import os
#####################
import requests
import json
#####################

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
    if req.get("result").get("action") != "room.booking":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("room-zone")
###################################
    spaceId = '18184'
    apiToken = 'NkPxt41IvOLJC80dhKYsuWy0JGRB7wSZRKlbU3MSPSbkTrOtI5iO7caLbtaZQg1LPMIqoYFaMagpFgVu5370Mzjv5JUrdUf1yL2HdGSUW3lL1XaaSs8VMLeaZlz8hyIm'
    url = 'https://api.robinpowered.com/v1.0/spaces/{}/presence'.format(spaceId)
###################################
    
    cost = {'Large Conference Room':'Conference Room 27NA, Conference Room 27S, Conference Rm 28NA, Conference Rm 28', 
            'Conference Room':'Conference Room 27NA, Conference Room 27NB, Conference Room 27S, Conference Rm 28NA, Conference Rm 28',
            'Small Conference Room':'Conference Room 27NB, Conference Room 28NB', 
            'Desk':'27D69, 27A23, 27D14',
           'Edit Room':'E-5A, E-6A, E-6C'}

    speech = "Available " + zone + " are " + str(cost[zone]) + "."

    
    
    
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
