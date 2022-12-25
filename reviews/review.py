import datetime
import json

keys_list = ['name', 'content', 'link', 'rating', 'time', 'owner_replied', 'owner_reply']

class Rev():
    name: str
    content: str
    link: str
    rating: int
    time: str
    owner_replied: bool
    owner_reply: str

    def __init__(self, raw_review: dict):
        self.name = raw_review[0][1]
        self.content = raw_review[3]
        self.link = raw_review[18]
        self.rating = raw_review[4]
        time_date_obj = datetime.datetime.utcfromtimestamp(round(raw_review[27]/1000, 0))
        self.time = str(time_date_obj)
        self.owner_replied = raw_review[9] is not None
        if self.owner_replied:
            self.owner_reply = raw_review[9][1]
        else:
            self.owner_reply = ""

    def __str__(self):
        positive_answer = f"Yes\n\nReply text from Owner:\n\"{self.owner_reply}\""
        return f"Reviewer Name: {self.name}\n\nReview content:\n\"{self.content}\"\n\nFull review link: {self.link}\n\nRating: {self.rating}\n\nReview Time Information: {self.time}\n\nDid the shop owner reply: {positive_answer if self.owner_replied else 'No'}"

    def dict(self):
        return self.__dict__

    def json_dump(self):
        return json.dumps(self.json())

    @classmethod
    def keys(self):
        return keys_list