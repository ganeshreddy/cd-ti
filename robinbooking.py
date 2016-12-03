import requests
import json

spaceId = 'your space ID here'
apiToken = 'your api token here'

url = 'https://api.robinpowered.com/v1.0/spaces/{}/presence'.format(spaceId)

# View all the presence in the space
response = requests.get( 
	url,
	headers={'content-type':'application/json', 'Authorization': 'Access-Token {}'.format(apiToken)}
	)

print(response.json())
