# https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html#backend-application-flow

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

client_id = 'm2m.client'
client_secret = '511536EF-F270-4058-80CA-1C89C192F69A'

client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

# Allowing for self-signed certificates. Don't do this in PROD!
oauth.verify = ''

token = oauth.fetch_token(
    token_url='https://localhost:5001/connect/token', 
    client_id=client_id,
    client_secret=client_secret)

print(token)