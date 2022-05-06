import pytest
from utils.http_requests import Http_Requests

requests = Http_Requests()
stationIds = [1,2,3,4,5]

@pytest.mark.parametrize('stationId', stationIds)
class TestAssignment:
    
    def test_verify_station_version(self, stationId):
        response = requests.get_station_version(stationId)

        assert response.get('status_code') == 200
        assert float(response.get('result')) > 1.6


    def test_verify_station_interval(self, stationId):
        response = requests.get_station_interval(stationId)

        assert response.get('status_code') == 200
        assert 1 <= float(response.get('result')) <= 60


    def test_set_value_minimum(self, stationId):
        response = requests.set_station_value(stationId, 2)

        assert response.get('status_code') == 200
        assert response.get('result') == 'OK'


    def test_set_value_maximum(self, stationId):
        response = requests.set_station_value(stationId, 10)

        assert response.get('status_code') == 200
        assert response.get('result') == 'OK'


    def test_set_value_lower_invalid_boundary(self, stationId):
        response = requests.set_station_value(stationId, 0)

        assert response.get('status_code') == 200
        assert response.get('result') == 'FAILED'


    def test_set_value_higher_invalid_boundary(self, stationId):
        response = requests.set_station_value(stationId, 11)

        assert response.get('status_code') == 200
        assert response.get('result') == 'FAILED'


    def test_set_value_string(self, stationId):
        response = requests.set_station_value(stationId, 'aa')

        assert response.get('status_code') == 200
        assert response.get('result') == 'FAILED'


    def test_set_value_empty(self, stationId):
        response = requests.set_station_value(stationId, '')

        assert response.get('status_code') == 200
        assert response.get('result') == 'FAILED'