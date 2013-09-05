import requests
from oauth_hook import OAuthHook
import json
class Buffer :
    API_BASE_URL = "https://api.bufferapp.com/1"
    FORMAT = "json"
    def __init__(access_token, access_key, consumer_key,
                 consumer_secret):

        oauth_hook = OAuthHook(access_token, access_key, consumer_key,
                               consumer_secret)
        self.requests_client = requests.session(hooks={'pre_request': oauth_hook})


    def get_user():
        request_url = "%s/user.%s" % (API_BASE_URL, FORMAT)
        response = self.requests_client.get(request_url)
        return response 

    def get_profiles():
        request_url = self.get_request_url("profile")
        resposne = self.requests_client.get(request_url)
        return response

    def get_profile(_id,extension=None):
        if extension is not None:
            endpoint = "/".join([_id, extension])
        else:
            endpoint = _id
        
        request_url = self.get_request_url("profile", endpoint)
        resposne = self.requests_client.get(request_url)
        return response

    def update_profile_schedule(_id, days, times):
        header = {"Content-Type": "application/json",}
        payload = [{"days": days,
                    "times": times,},]
        payload = json.dumps(payload)
        if extension is not None:
            endpoint = "/".join([_id, extension])
        else:
            endpoint = _id
        
        request_url = self.get_request_url("profile", endpoint)
        response = self.requests.post(request_url, data=payload,
                                      headers=headers)
        return response
    
    def get_shares(url):
        request_url = self.get_request_url("shares")
        payload = {"url": url,}
        resposne = self.requests_client.get(request_url, params=payload)
        return response

    def get_config():
        request_url = self.get_request_url("config")
        resposne = self.requests_client.get(request_url)
        return response

    def get_updates(_id, extension=None):
        if extension is not None:
            endpoint = "/".join([_id, extension])
        else:
            endpoint = _id
        
        request_url = self.get_request_url("updates", endpoint)
        resposne = self.requests_client.get(request_url)
        return response

    def update(_id,extension):
        if extension is not None:
            endpoint = "/".join([_id, extension])
        else:
            endpoint = _id
        
        request_url = self.get_request_url("update", endpoint)
        response = self.requests.post(request_url)
        return response

    def get_profile_updates(_id, extension):
        endpoint = "/".join([_id, "updates", extension])
        request_url = self.get_request_url("profile", endpoint)
        resposne = self.requests_client.get(request_url)
        return response

    def update_profile(_id, extension,params):
        endpoint = "/".join([_id, "updates", extension])
        request_url = self.get_request_url("profile", endpoint)
        response = self.requests_client.post(request_url, params)
        return response


