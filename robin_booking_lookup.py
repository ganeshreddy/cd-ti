import requests
import json

spaceId = 'your space ID here'
apiToken = 'NkPxt41IvOLJC80dhKYsuWy0JGRB7wSZRKlbU3MSPSbkTrOtI5iO7caLbtaZQg1LPMIqoYFaMagpFgVu5370Mzjv5JUrdUf1yL2HdGSUW3lL1XaaSs8VMLeaZlz8hyIm'

# url = 'https://api.robinpowered.com/v1.0/spaces/{}/presence'.format(spaceId)
url = 'https://api.robinpowered.com/v1.0/free-busy/spaces?location_ids=4495'


# View all the presence in the space
response = requests.get( 
	url,
	headers={'content-type':'application/json', 'Authorization': 'Access-Token {}'.format(apiToken)}
	)

print(response.json())
