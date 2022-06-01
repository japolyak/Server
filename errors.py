class APIError(Exception):
    def __init__(self, status, message):
        Exception.__init__(self)
        self.status = status
        self.message = message
