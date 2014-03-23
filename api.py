import requests
from rauth import OAuth2Session
from utils import normalize_for_extension, patch_params_for_requests 
import json

class Buffer :
    API_BASE_URL = "https://api.bufferapp.com/1"
    FORMAT = "json"
    CATEGORY_URL_MAPPING = {'user':'user',
                            'profiles' : 'profiles',
                            'updates' : 'updates',
                            'shares' : 'links/shares',
                            'config': 'info/configuration',}

    def __init__(self,access_token, client_id, client_secret):
        self.requests_client = OAuth2Session(client_id=client_id,
                client_secret=client_secret,
                access_token=access_token)

    def get_request_url(self,category, endpoint=None):
        request_url = "/".join([self.API_BASE_URL,
                                self.CATEGORY_URL_MAPPING[category]])
        if endpoint is None:
            request_url = "%s.%s" % (request_url, self.FORMAT)
        else:
            request_url = "%s/%s.%s" % (request_url, endpoint, self.FORMAT)
        return request_url


    def get_user(self):
        request_url = "%s/user.%s" % (self.API_BASE_URL, self.FORMAT)
        response = self.requests_client.get(request_url).json()
        return response 

    def get_profiles(self):
        request_url = self.get_request_url("profiles")
        response = self.requests_client.get(request_url).json()
        return response


    def get_profile(self,_id,extension=None):
        endpoint = normalize_for_extension(_id, extension)
        request_url = self.get_request_url("profiles", endpoint)
        response = self.requests_client.get(request_url).json()
        return response
    
    
    def update_profile_schedule(self,_id, days, times):
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
        schedule_format = "schedules[0][%s][]=%s&"
        payload = ""
        for day in days:
            payload += schedule_format %("days", day)
        for time in times:
            payload += schedule_format %("times", time)
        endpoint = normalize_for_extension(_id, "schedules/update")
        request_url = self.get_request_url("profiles", endpoint)
        response = requests.post(request_url, data=payload, headers=headers)
        return response

    def get_shares(self,url):
        request_url = self.get_request_url("shares")
        payload = {"url": url,}
        response = self.requests_client.get(request_url, params=payload).json()
        return response

    def get_config(self):
        request_url = self.get_request_url("config")
        response = self.requests_client.get(request_url).json()
        return response

    def get_updates(self,_id, extension=None, params={}):
        endpoint = normalize_for_extension(_id, extension)
        request_url = self.get_request_url("updates", endpoint)
        response = self.requests_client.get(request_url, params=params).json()
        return response

    
    def get_profile_updates(self,_id, extension, params={}):
        endpoint = "/".join([_id, "updates", extension])
        request_url = self.get_request_url("profiles", endpoint)
        response = self.requests_client.get(request_url,
                params=params).json()
        return response

    def update_profile(self,_id, extension,params={}):
        endpoint = "/".join([_id, "updates", extension])
        request_url = self.get_request_url("profiles", endpoint)
        params = patch_params_for_requests(params)
        response = self.requests_client.post(request_url, data=params)
        return response


    def update(self,_id, extension, params):
        endpoint = normalize_for_extension(_id, extension)
        request_url = self.get_request_url("updates", endpoint)
        params = patch_params_for_requests(params)
        response = self.requests_client.post(request_url, data=params)
        return response
    
    def create_update(self, params):
        request_url = self.get_request_url("updates", "create")
        params = patch_params_for_requests(params)
        response = self.requests_client.post(request_url, data=params)
        return response
