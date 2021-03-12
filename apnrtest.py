import requests
from pprint import pprint
import json
regions = ['au'] # Change to your country
with open('/home/ronan/Documents/image1.jpg', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token 6916516f3ef2eb4dadea6c911b3ff3538ed91158'})
r.json()
print(response['plate'])
pprint(response.json())
