import requests
import simplejson
from requests.auth import HTTPProxyAuth

from myqiwi import exceptions

API_URl = "https://edge.qiwi.com/"

proxy = {}


def send(path, params=None, method="get", json=None, proxy=None, headers={}):
    url = API_URl + path

    if proxy is not None:
        kwargs = {
            "proxies": {"http": proxy["http"]},
            "auth": HTTPProxyAuth(proxy["username"], proxy["password"])
    }
    else:
        kwargs = {}

    response = requests.request(method.upper(), url, params=params, json=json, headers=headers, **kwargs)

    try:
        data = response.json()
    except simplejson.errors.JSONDecodeError:
        data = {"code": None, "message": None}

    if response.status_code in [400, 401, 403, 404]:
        error_text = response.text

        if "code" in data:
            code = data["code"]
            message = data["message"]
        else:
            code = data["errorCode"]
            message = data["userMessage"]

        if 400 == response.status_code:
            raise exceptions.ArgumentError(error_text, code, message)
        if 401 == response.status_code:
            raise exceptions.InvalidToken("Invalid token", code, message)
        if 403 == response.status_code:
            raise exceptions.NotHaveEnoughPermissions(error_text, code, message)
        if 404 == response.status_code:
            raise exceptions.NoTransaction(error_text, code, message)

    return data
