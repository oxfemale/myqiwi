from .. import exceptions

class BaseBackEnd:
    API_URl = "https://edge.qiwi.com/"

    def __init__(self):
        self.proxy = None

    def validate_response(self, response):
        data = response.json

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

    @staticmethod
    def make_url(path):
        return BaseBackEnd.API_URl + path
