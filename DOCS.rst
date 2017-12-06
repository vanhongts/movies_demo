================
SERVERLESS DEMO
================
We will deploy project via command::

 sls deploy

And it reports::

    Service Information
    service: movies
    stage: dev
    region: xxxx
    stack: movies-dev
    api keys:
      None
    endpoints:
      POST - https://xxxxxx/dev/movies
      GET - https://xxxxxx/dev/movies
      GET - https://xxxxxx/dev/movies/get
    functions:
      create: movies-dev-create
      list: movies-dev-list
      get: movies-dev-get


We create a file index.html and stored it in AWS S3. From index.html, we wrote some jquery function to call Aws Api Gateway.

This example used PynamoDB to access DynamoDB, aws lambda python to write code, Serverless framework to deploy to aws cloud. We hope that is helpful for you


