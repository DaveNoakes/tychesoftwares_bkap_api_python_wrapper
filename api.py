"""
Tychesoftwares Bookings and Appointments API Class. 
Heavily inspired by the WooCommerce API class from the woocommerce package by Claudio Sanches @ Automattic.
"""

__title__ = "tychesoftwares-bkap-api"
__version__ = "1.0.0"
__author__ = "David Noakes"
__license__ = "MIT"

from requests import request, HTTPError
from requests.auth import HTTPBasicAuth
from json import dumps as jsonencode


class BkapAPI:
    """ Bkap API Class """

    def __init__(self, url: str, consumer_key: str, consumer_secret: str, **kwargs):
        self.url = url.rstrip('/')
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.verify_ssl = kwargs.get("verify_ssl", True)
        self.timeout = kwargs.get("timeout", 5)
        self.user_agent = kwargs.get(
            "user_agent", f"Bookings-Python-REST-API/{__version__}")

    def __get_url(self, endpoint):
        """ Get URL for requests """
        if endpoint.startswith('/'):
            endpoint = endpoint.lstrip('/')
        return f"{self.url}/wc-api/v3/bkap/{endpoint}"

    def __request(self, method, endpoint, data=None, params=None):
        """ Do requests """
        url = self.__get_url(endpoint)
        headers = {
            "user-agent": self.user_agent,
            "accept": "application/json"
        }
        auth = HTTPBasicAuth(self.consumer_key, self.consumer_secret)

        if data is not None:
            data = jsonencode(data, ensure_ascii=False).encode('utf-8')
            headers["content-type"] = "application/json;charset=utf-8"

        response = request(
            method=method,
            url=url,
            auth=auth,
            params=params,
            data=data,
            timeout=self.timeout,
            headers=headers,
            verify=self.verify_ssl
        )
        try:
            response.raise_for_status()
        except HTTPError as e:
            # Log or print HTTP error details
            print(f"HTTP error occurred: {e}")
            print("Response status:", response.status_code)
            print("Response text:", response.text)
            return HTTPError
        return response.json()

    def get(self, endpoint, params=None):
        """ Get requests """
        return self.__request("GET", endpoint, params=params)

    def post(self, endpoint, data, params=None):
        """ POST requests """
        return self.__request("POST", endpoint, data=data, params=params)

    def put(self, endpoint, data, params=None):
        """ PUT requests """
        return self.__request("PUT", endpoint, data=data, params=params)

    def delete(self, endpoint, params=None):
        """ DELETE requests """
        return self.__request("DELETE", endpoint, params=params)
