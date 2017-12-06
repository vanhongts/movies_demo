from datetime import datetime
import os
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute, NumberAttribute, UnicodeSetAttribute, UTCDateTimeAttribute, MapAttribute,ListAttribute
)

class Info(MapAttribute):
    """a example of info
            "info": {
                "actors": [
                    "Daniel VVH",
                    "Chris VVH",
                    "Olivia VVH"
                ],
                "release_date": "2017-11-03T11:39:44.659235+0000",
                "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
                "genres": [
                    "Action",
                    "Biography",
                    "Drama",
                    "Sport"
                ],
                "image_url": "http://hong.com.vn/hong.jpg",
                "directors": [
                    "VVH"
                ],
                "rating": 8.3,
                "rank": 2,
                "running_time_secs": 7380
            }
    """
    directors = ListAttribute()
    release_date = UTCDateTimeAttribute()
    rating = NumberAttribute()
    genres = ListAttribute()
    image_url = UnicodeAttribute()
    plot = UnicodeAttribute()
    rank = NumberAttribute()
    running_time_secs = NumberAttribute()
    actors = ListAttribute()

class Movie(Model):
    '''
    A example of Movie:
    {
        "title": "Testing of Hong",
        "year": 1985,
        "info": {
            "actors": [
                "Daniel VVH",
                "Chris VVH",
                "Olivia VVH"
            ],
            "release_date": "2017-11-03T11:39:44.659235+0000",
            "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
            "genres": [
                "Action",
                "Biography",
                "Drama",
                "Sport"
            ],
            "image_url": "http://hong.com.vn/hong.jpg",
            "directors": [
                "VVH"
            ],
            "rating": 8.3,
            "rank": 2,
            "running_time_secs": 7380
        }
    }

    '''
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        if os.environ['IS_OFFLINE']:
            host = 'http://localhost:8000'
        else:
            region = 'ap-southeast-1'
            host = 'https://dynamodb.ap-southeast-1.amazonaws.com'

    year = NumberAttribute(hash_key=True)
    title = UnicodeAttribute(range_key=True)
    info = Info()
    def save(self, conditional_operator=None, **expected_values):
        super(Movie, self).save()
    def __iter__(self):
        for name, attr in self._get_attributes().items():
            yield name, attr.serialize(getattr(self, name))



