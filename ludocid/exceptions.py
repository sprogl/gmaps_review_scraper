
class BadSearch(Exception):
    "Exception raised when the search returns no unique result"

    def __init__(self):
        super().__init__("no unique search result returned")

class NoDriver(Exception):
    "Exception raised when firefox driver could not be found"

    def __init__(self):
        super().__init__("firefox driver could not be found")
