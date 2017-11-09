import json
import logging
import uuid
import decimal
from datetime import datetime
from dateutil import parser
from movies.MovieModel import Movie
from movies.MovieModel import Info
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def create(event, context):
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


    #data = event
    data = json.loads(event['body'])  #uncomment when upload to AWS
    if "title" not in data:
        logging.error('Validation Failed')
        return {'statusCode': 422
                , 'headers': {
                        "Access-Control-Allow-Origin" : "*", 
                        "Access-Control-Allow-Credentials" : True 
                },
                'body': json.dumps({'error_message': 'Couldn\'t create the movie item.'})}

    if not data["title"]:
        logging.error('Validation Failed - text was empty. %s', data)
        return {'statusCode': 422
                , 'headers': {
                        "Access-Control-Allow-Origin" : "*",
                        "Access-Control-Allow-Credentials" : True
                }
                , 'body': json.dumps({'error_message': 'Couldn\'t create the todo item. As text was empty.'})}

    info = Info(directors= data["info"]["directors"],
                release_date= parser.parse(data["info"]['release_date']),
                rating= data["info"]['rating'],
                genres= data["info"]['genres'],
                image_url= data["info"]['image_url'],
                plot= data["info"]['plot'],
                rank= data["info"]['rank'],
                running_time_secs= data["info"]['running_time_secs'],
                actors= data["info"]['actors'],
            )
    movie = Movie(
        year=data['year'],
        title=data['title'],
        info=info)
    movie.save()

    # create a response
    return {'statusCode': 201,
                'headers': {
                    "Access-Control-Allow-Origin" : "*",
                    "Access-Control-Allow-Credentials" : True
                  },
            'body': json.dumps(dict(movie))}
