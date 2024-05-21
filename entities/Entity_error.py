from entities.Base_error import BaseError

class ParamNotValidated(BaseError):
    def __init__(self, param: str, message: str):
        super().__init__(f'Field {param} is wrong: {message}')