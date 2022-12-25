import scrapy
import scrapy.http
import json
import csv
import collections.abc
import reviews.review

class ReviewSpider(scrapy.Spider):
    _url_fragments = ["https://www.google.com/maps/preview/review/listentitiesreviews?pb=!1m1!2y", "!2m1", "!2m2!3s", "!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m1!7e81"]

    def __init__(self, ludocid, csv_filename="reviews.csv", name="review",**kwargs):
        if name is not None:
            self.name = name
        elif not getattr(self, "name", None):
            raise ValueError(f"{type(self).__name__} must have a name")
        self.__dict__.update(kwargs)

        self._id_next_review = ""
        self._cont = True
        self.ludocid = ludocid
        
        self._csv_file = open(csv_filename, "w")
        self._writer = csv.DictWriter(self._csv_file, fieldnames=reviews.review.Rev.keys())
        self._writer.writeheader()        

    def start_requests(self):
        yield scrapy.http.Request(self.url(), callback=self.parse, dont_filter=True)


    def url(self):
        if self._id_next_review:
            return f"{self._url_fragments[0]}{self.ludocid}{self._url_fragments[2]}{self._id_next_review}{self._url_fragments[3]}"
        else:
            return f"{self._url_fragments[0]}{self.ludocid}{self._url_fragments[1]}{self._url_fragments[3]}"

    def parse(self, response):
        try:
            reviews_raw = json.loads(response.text[5:])[2]
        except TypeError:
            return
        if isinstance(reviews_raw, collections.abc.Iterable):
            for rev_raw in reviews_raw:
                rev_rendered = reviews.review.Rev(rev_raw)
                self._writer.writerow(rev_rendered.dict())
                try:
                    self._id_next_review = rev_raw[61]
                except IndexError:
                    return
            return scrapy.http.Request(self.url(), callback=self.parse, dont_filter=True)
        else:
            return

    def __del__(self):
        self._csv_file.close()