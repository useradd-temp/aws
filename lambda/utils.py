import json
import os


def get_value_from_store(poolManager, key):
    
    url = 'http://localhost:2773/systemsmanager/parameters/get'
    headers = {'X-Aws-Parameters-Secrets-Token': os.environ.get('AWS_SESSION_TOKEN')}
    query_params = {'name': key}
    
    response = poolManager.request('GET', url, fields=query_params, headers=headers)
    decode_response = response.data.decode('utf-8')
    
    return json.loads(decode_response).get('Parameter', dict()).get('Value', None)
    