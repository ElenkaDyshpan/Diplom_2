import requests


class BaseHttpClient:
    @staticmethod
    def get(url, params=None, headers=None):
        return requests.get(url, params=params, headers=headers)

    @staticmethod
    def post(url, data=None, headers=None):
        return requests.post(url, data=data, headers=headers)

    @staticmethod
    def put(url, params=None, headers=None):
        return requests.put(url, params=params, headers=headers)

    @staticmethod
    def delete(url, params=None, headers=None):
        return requests.get(url, params=params, headers=headers)