
class Error(Exception):
    pass

class RegistrationError(Error):

    def __init__(self, message):
        self.message = message