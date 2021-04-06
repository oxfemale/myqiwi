import requests
from requests.auth import HTTPProxyAuth

from .base import BaseBackEnd


class RequestBackEnd(BaseBackEnd):
    async def post(self, *args, **kwargs):
        return self.request(*args, **kwargs, method="post")

    async def get(self, *args, **kwargs):
        return self.request(*args, **kwargs, method="get")

    def request(self, path, params=None, json=None, method="get"):
        url = self.make_url(path)

        if proxy is not None:
            kwargs = {
                "proxies": {"http": "{}:{}".format(self.proxy["ip"], self.proxy["port"])},
                "auth": HTTPProxyAuth(proxy["username"], proxy["password"])
            }
        else:
            kwargs = {}

        response = requests.request(method.upper(), url, params=params, json=json, headers=headers, **kwargs)
        return self.validate_response(_response)