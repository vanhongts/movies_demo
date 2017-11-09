import json
import logging
from datetime import datetime
from dateutil import parser
from movies.MovieModel import Movie
from movies.MovieModel import Info
from pynamodb.exceptions import DoesNotExist


def update(event, context):
    # TODO: Figure out why this is behaving differently to the other endpoints
    # data = json.loads(event['body'])
    data = event;
    #data = event['body'] # TODO uncomment when up to AWS
    info = data['info']
    if 'title' not in data and 'year' not in data:
        logging.error('Validation Failed %s', data)
        return {'statusCode': 422
                , 'headers': {
                        "Access-Control-Allow-Origin" : "*", 
                        "Access-Control-Allow-Credentials" : True 
                },
                'body': json.dumps({'error_message': 'Couldn\'t update the movie item.'})}

    try:
        found_movie = Movie.get(data['year'], data['title'])
    except DoesNotExist:
        return {'statusCode': 404
                , 'headers': {
                        "Access-Control-Allow-Origin" : "*", 
                        "Access-Control-Allow-Credentials" : True 
                },
                'body': json.dumps({'error_message': 'MOVIE was not found'})}

    movie_changed = True

    if movie_changed:
        parser.parse(info['release_date'])
        found_movie.info = info
        found_movie.info.release_date = parser.parse(found_movie.info.release_date)
        found_movie.save()
    else:
        logging.info('Nothing changed did not update')

    # create a response
    return {'statusCode': 200
             , 'headers': {
                        "Access-Control-Allow-Origin" : "*", 
                        "Access-Control-Allow-Credentials" : True 
                },
            'body': json.dumps(dict(found_movie))}
