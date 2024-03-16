import requests
import json

"""
Insert app_id and app_secret for your Facebook Page
Create a permanent/long-term token for creds['access_token'] 
"""

def getCreds():
    app_id = ' '
    app_secret = ' '
    creds = dict()
    creds['access_token'] = " "
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v19.0'
    creds["endpoint_base"] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['instagram_account_id'] = '17841464666256501'
    return creds

def makeApiCall(url, endpointParams, type):

    if type == 'POST':
        data = requests.post(url, endpointParams)
    else:
        data = requests.get(url,endpointParams)
    
    response = dict()
    response['url']=url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams,indent = 4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'],indent = 4)

    return response