#this is for primmordial
import webbrowser
import msal
from msal import PublicClientApplication

APPLICATION_ID = '589f079e-5345-40f9-ba6b-c264c0070d43'
CLIENT_SECRET = 'bSc8Q~CK-FIJ7AJvs3wSa6AutA.JRnRAtxqZHcV_'
authority_url = 'https://login.microsoftonline.com/consumers/'
base_url = 'https://graph.microsoft.com/v1.0/me'

endpoint = base_url + 'me'
SCOPES = ['User.Read', 'User.Export.All']

client_instance = msal.ConfidentialClientApplication(
    client_id=APPLICATION_ID,
    client_credential=CLIENT_SECRET,
    authority=authority_url
)
