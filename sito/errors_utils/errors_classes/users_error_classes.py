class UserAlreadyExists(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InitPasswordNotSet(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
