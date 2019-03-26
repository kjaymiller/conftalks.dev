import requests
import json
from config import MAILCHIMP_KEY, AIRTABLE_API

content_type='application/json'

# Connect to AirTable
headers = {'Authorization': f'Bearer {AIRTABLE_API}'}
url = 'https://api.airtable.com/v0/appuFBQpMhzKDXSHn/Developers'

# Get AirTable Members
r = requests.get(url, headers=headers)
airtable_devs = ([e['fields']['Email'] for e in r.json()['records']])


#Connect to Mailchimp
list_id = 'f6ecfc7b5d'
headers = {
        'content-type': content_type,
       'Authorization': f'apikey {MAILCHIMP_KEY}',
        }

base_chimp_url = f'https://us19.api.mailchimp.com/3.0/lists/{list_id}'
members_url = f'{base_chimp_url}/members'

# Get MailChimp Subscribers
r = requests.get(members_url, headers=headers)
mailchimp_subs = (e for e in r.json()['members'])

users_to_tag = filter(lambda x: x['email_address'] in airtable_devs, mailchimp_subs)

segment_id = '33655'
tags_url = f'{base_chimp_url}/segments/{segment_id}'
data = json.dumps({"members_to_add": list(map(lambda x:x['email_address'], users_to_tag))}) 
r = requests.post(tags_url, headers=headers, data=data)
print(r.json())


