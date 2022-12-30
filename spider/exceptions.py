
class UnexpectedFormat(Exception):
    "Exception raised when the api returns an unexpectected response format"

    def __init__(self):
        super().__init__("unexpected api response format")