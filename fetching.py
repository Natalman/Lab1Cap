import json
import requests
try:
    r = requests.get('http://www.omdbapi.com/?t=IP+man&y=&plot=short&r=json')
    r.status_code
except Timeout:
    print('The server is unreachable, Please try later')
except ConnectionError:
    print('Connection error occured')
except HTTPError:
    print('HTTP error occurs')

r.json()
print(r)
