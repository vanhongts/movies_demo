import json
import logging
import uuid
import decimal
from datetime import datetime
from dateutil import parser
from movies.MovieModel import Movie
from movies.MovieModel import Info
from dynamodb_json import json_util as pjson

def list(event, context):
    '''
    info = Info(directors= ["VVH"],
                release_date= datetime.now(),
                rating= 8.3,
                genres= [
                    "Action",
                    "Biography",
                    "Drama",
                    "Sport"
                ],
                image_url= "http://hong.com.vn/hong.jpg",
                plot= "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
                rank= 2,
                running_time_secs= 7380,
                actors= [
                    "Daniel VVH",
                    "Chris VVH",
                    "Olivia VVH"
                ]
            )
    movie = Movie(
        year=1986,
        title='test of Bu',
        info=info)
    '''
    # fetch all todos from the database
    results = Movie.scan()

    # create a response
    return {'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin" : "*", 
                "Access-Control-Allow-Credentials" : True                       
              },
             'body': json.dumps({'movies': [pjson.loads(dict(result)) for result in results]})}

    
