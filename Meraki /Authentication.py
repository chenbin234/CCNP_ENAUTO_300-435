from requests import Session
class NoRebuildAuthSession(Session):
    def rebuild_auth(self, prepared_request, response):
      '''
      No code here means requests will always preserve the Authorization header when redirected.
      Be careful not to leak your credentials to untrusted hosts!
      '''
session = NoRebuildAuthSession()
API_KEY = 'bc9bd39b9f924e36ced499f8b4511d10e1fa2569'
response = session.get('https://api.meraki.com/api/v1/organizations/', headers={'Authorization': f'Bearer {API_KEY}'})
print(response.json())
