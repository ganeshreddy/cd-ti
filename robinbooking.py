import requests
import json

spaceId = '18184'
apiToken = 'NkPxt41IvOLJC80dhKYsuWy0JGRB7wSZRKlbU3MSPSbkTrOtI5iO7caLbtaZQg1LPMIqoYFaMagpFgVu5370Mzjv5JUrdUf1yL2HdGSUW3lL1XaaSs8VMLeaZlz8hyIm'

url = 'https://api.robinpowered.com/v1.0/spaces/{}/presence'.format(spaceId)

# View all the presence in the space
response = requests.get( 
	url,
	headers={'content-type':'application/json', 'Authorization': 'Access-Token {}'.format(apiToken)}
	)

print(response.json())
