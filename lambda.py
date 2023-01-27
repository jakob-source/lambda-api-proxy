import json
import urllib3
import warnings
from botocore.vendored import requests
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def lambda_handler(event, context):
    url = "<internal_server_url>"
    if event.get('httpMethod'):
        http_method = event['httpMethod']

    headers = ''
    if event.get('headers'):
        headers = event['headers']


    if event.get('path'):
        path = event['path']
        
    body = ''
    if event.get('body'):
        body = event['body']
    try:
        response = requests.post(url+path, data=body, verify=False)
        r = {
            "isBase64Encoded": False,
            "statusCode": response.status_code,

            "body": json.dumps(response, default=str)   
                }
    except:
        print('Connection failed.')
        r = {
            "isBase64Encoded": False,
            "statusCode": response.status_code,
            "body": "Connection failed."   
                }
    return r
