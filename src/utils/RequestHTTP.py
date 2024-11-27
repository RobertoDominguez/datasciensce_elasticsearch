import requests
from utils.DataResponse import DataResponse
import json


class RequestHTTP:
    def __init__(self, base_url):
        self.base_url = base_url  # URL base para las peticiones

    def GET(self, endpoint, params=None, headers=None, callback=None):
        try:
            response = requests.get(f"{self.base_url}{endpoint}", params=params, headers=headers)
            data_response = DataResponse(None, False, response.status_code, "", response.headers)
            
            if callback and response.status_code>=200 and response.status_code<300:
                data_response.setData( callback( json.loads(response.text )) )
                data_response.setStatus(True)
            return data_response

        except requests.RequestException as e:
            error_response = DataResponse(None, False, 500, str(e), None)
            print(str(e))
            return error_response

    def POST(self, endpoint, data=None, headers=None, callback=None):
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)
            data_response = DataResponse(response.json(), False, response.status_code, response.headers)
            
            if callback and response.status_code>=200 and response.status_code<300:
                data_response.setData( callback( json.loads(response.text )) )
                data_response.setStatus(True)
            return data_response

        except requests.RequestException as e:
            error_response = DataResponse(None, False, 500, str(e), None)
            print(str(e))
            return error_response

    def PUT(self, endpoint, data=None, headers=None, callback=None):
        try:
            response = requests.put(f"{self.base_url}{endpoint}", json=data, headers=headers)
            data_response = DataResponse(response.json(), False, response.status_code, response.headers)
            
            if callback and response.status_code>=200 and response.status_code<300:
                data_response.setData( callback( json.loads(response.text )) )
                data_response.setStatus(True)
            return data_response

        except requests.RequestException as e:
            error_response = DataResponse(None, False, 500, str(e), None)
            print(str(e))
            return error_response

    def DELETE(self, endpoint, headers=None, callback=None):
        try:
            response = requests.delete(f"{self.base_url}{endpoint}", headers=headers)
            data_response = DataResponse(response.json(), False, response.status_code, response.headers)
            
            if callback and response.status_code>=200 and response.status_code<300:
                data_response.setData( callback( json.loads(response.text )) )
                data_response.setStatus(True)
            return data_response

        except requests.RequestException as e:
            error_response = DataResponse(None, False, 500, str(e), None)
            print(str(e))
            return error_response
