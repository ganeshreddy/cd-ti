#!/usr/bin/env python

import urllib
import json
import os
######################
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
    """    
    if req.get("result").get("action") != "room.availability":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("room-zone")
    #zone = 'Conference Room'   
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

    if val['data'] == []:
        print 'No Data!'
    else:
        for rows in val['data']:
            if zone.lower() in str(rows['space']['name'].lower()):
                retntxt= zone + ' ' + retntxt + rows['space']['type'] + ' type - ' + rows['space']['name'] + ' (' + str(rows['space']['capacity']) + ' person capacity)'  + ', Location Id ' + str(rows['space']['location_id']) + ', Space Id ' + str(rows['space']['id']) + '\n'        
        
                print retntxt
        
    return {
            "speech": retntxt,
            "displayText": retntxt,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-roombooking"
        }
    """
#####################################
    if req.get("result").get("action") != "room.book":
        return {}
    result = req.get("result")
    #parameters = result.get("parameters")
    params = {"id": "18185", "ended_at": "2016-12-11T19:00:00Z", "started_at": "2016-12-11T18:00:00Z", "title": "scheduled from API 1.0", "user_ref": "50078"}
    #zone = parameters.get("room-zone")
    spaceid = 18185 #parameters.get("id")
    #zone = 'Conference Room'   
    #spaceId = '4495'
    apiToken = 'NkPxt41IvOLJC80dhKYsuWy0JGRB7wSZRKlbU3MSPSbkTrOtI5iO7caLbtaZQg1LPMIqoYFaMagpFgVu5370Mzjv5JUrdUf1yL2HdGSUW3lL1XaaSs8VMLeaZlz8hyIm'

    url = 'https://api.robinpowered.com/v1.0/spaces/'+ str(spaceid) + '/events'
    # View all the presence in the space
    r = requests.post( 
        url,
        params=params, 
        headers={'content-type':'application/json', 'Authorization': 'Access-Token {}'.format(apiToken)}
        )
    
    retntxt = r.json()  
    print url
    print result
        
    return {
            "speech": retntxt,
            "displayText": retntxt,
            #"data": {},
            # "contextOut": [],
            "source": "apiai-roombooking"
        }    
##################################### 

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
