#!/usr/bin/env python

import urllib
import json
import os
#####################
import requests
######################

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

    spaceId = '4495'
    apiToken = 'NkPxt41IvOLJC80dhKYsuWy0JGRB7wSZRKlbU3MSPSbkTrOtI5iO7caLbtaZQg1LPMIqoYFaMagpFgVu5370Mzjv5JUrdUf1yL2HdGSUW3lL1XaaSs8VMLeaZlz8hyIm'

    url = 'https://api.robinpowered.com/v1.0/free-busy/spaces?include=state&location_ids='+ spaceId
    # View all the presence in the space
    r = requests.get( 
	    url,
	    headers={'content-type':'application/json', 'Authorization': 'Access-Token {}'.format(apiToken)}
	    )
    val = json.loads(r.text)

    retntxt = ''
    zone = 'Desk'	
    
    if val['data'] == []:
        print 'No Data!'
    else:
        for rows in val['data']:
		if zone.lower() in str(rows['space']['name'].lower()):
		    retntxt= retntxt + rows['space']['type'] + ' type - ' + rows['space']['name'] + ' (' + str(rows['space']['capacity']) + ' person capacity)'  + ', Location Id ' + str(rows['space']['location_id']) + ', Space Id ' + str(rows['space']['id']) + '\n'        
        
	            print retntxt
		
    return {
            "speech": retntxt,
            "displayText": retntxt,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-roombooking"
	    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
