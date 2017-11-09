import json
import logging
from datetime import datetime
from dateutil import parser
from movies.MovieModel import Movie
from movies.MovieModel import Info
from pynamodb.exceptions import DoesNotExist
from dynamodb_json import json_util as json



def get(event, context):
    data = event;
    #data = event['body'] # TODO uncomment when up to AWS
    try:
        found_movie = Movie.get(data['year'], data['title'])
    except DoesNotExist:
        return {'statusCode': 404
                , 'headers': {
                    "Access-Control-Allow-Origin" : "*", 
                    "Access-Control-Allow-Credentials" : True 
                },
                'body': json.dumps({'error_message': 'MOVIE was not found'})}

    # create a response
    return {'statusCode': 200
                    , 'headers': {
                        "Access-Control-Allow-Origin" : "*", 
                        "Access-Control-Allow-Credentials" : True 
                },
            'body': json.loads(dict(found_movie))}
