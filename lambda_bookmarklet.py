import json
from urllib.request import urlopen, Request


def lambda_handler():
    raw_data = {'fields':{
            "Conference Name": 'Conference Name',
            "Website": 'Website',
            "Added By": 'Added By',
        }}

    headers = {
            "authorization": "Bearer keyOzyWXah5fdzUL1",
            "content-type": "application/json"
            }

    body = json.dumps(raw_data).encode('utf-8')

    req = Request(
            method='POST',
            url='https://api.airtable.com/v0/appuFBQpMhzKDXSHn/Conferences',
            headers=headers,
            data=body,
            )

    res = urlopen(req)
    return res.status, res.text

print(lambda_handler())
