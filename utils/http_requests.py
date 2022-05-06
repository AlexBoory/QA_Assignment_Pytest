import requests
import json

class Http_Requests:
    baseUrl = "https://api-energy-k8s.test.virtaglobal.com/"
    timeout = 3


    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    @staticmethod
    def getResult(response):
        responseJson = response.json()

        return {
            'result': responseJson.get('result'),
            'status_code': response.status_code
        }
    

    @staticmethod
    def station_path(stationId):
        return f'v1/tests/{stationId}'


    def post(self, stationId, reqBody):
        response = requests.post(self.baseUrl + self.station_path(stationId), headers=self.headers, timeout=self.timeout, json=reqBody)

        return self.getResult(response)


    def get_station_version(self, stationId):
        response = self.post(stationId, json.loads('{"command": "getVersion"}'))

        return response


    def get_station_interval(self, stationId):
        response = self.post(stationId, json.loads('{"command": "getInterval"}'))

        return response


    def set_station_value(self, stationId, value):
        reqBody = {
            "command": "setValues",
            "payload": value
        }

        response = self.post(stationId, reqBody)

        return response