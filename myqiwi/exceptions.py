class BaseQiwiException(Exception):
    def __init__(self, qiwi_text_response, code, message):
        super(BaseQiwiException, self).__init__(qiwi_text_response)
        self.code = code
        self.message = message


class ArgumentError(BaseQiwiException):
    pass


class InvalidToken(BaseQiwiException):
    pass


class NotHaveEnoughPermissions(BaseQiwiException):
    pass


class NoTransaction(BaseQiwiException):
    pass


class NeedPhone(BaseQiwiException):
    pass


class CurrencyInvalid(BaseQiwiException):
    pass
