
import requests
import json
from apikey import api_key

'''
publishedAfter	datetime
The publishedAfter parameter indicates that the API response should only contain resources created at or after the specified time.
 The value is an RFC 3339 formatted date-time value (1970-01-01T00:00:00Z).
 
 https://stackoverflow.com/questions/8556398/generate-rfc-3339-timestamp-in-python

'''

from datetime import datetime, timezone
local_time = datetime.now(timezone.utc).astimezone()
local_time.isoformat()
print(local_time)

search_time = "2020-03-18%2022:16:14.418001-04:00"

url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=49&&q=quitar%20lessons&key=' + api_key

headers = {'Accept': 'application/json'}
req = requests.get(url, headers=headers)
jreq = req.json()
print(jreq)




