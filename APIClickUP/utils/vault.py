"""
This script is used to get the token from the vault server.
"""
import hvac

def get_token():
    """
    Method to get the token from the vault server
    """
    client = hvac.Client(url='http://127.0.0.1:8200',
                         token='dev-only-token')
    read_response = client.secrets.kv.read_secret_version(path='secret_token')
    token = read_response['data']['data']['todo_token']
    print(token)
    return token

get_token()
