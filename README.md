# Introduction

This repo is a very simple app for show off purposes. The application was coded with flask framework for the api and redis as a queue manager.

It has no user interface, the only possible way to send requests to th producer api endpoint is through command line requests or postman.

Although simple, the app is provided with a gunicorn socket and nginx server. Its main structure is as follows: A producer flask server exposes a post endpoint through which gets json data and lines it up in a redis queue. A consumer server sets up a redis worker that gets the jobs and pastes the json data in a output.txt file.

# How to run

## Dependencies

Both the consumer and the producer services/folders have their own `requirements.txt` file but the producer service is a superset of both. There you can see all the libraries needed for the project.

## Starting the app

To build and start the app:
`docker-compose -f docker-compose.yml up --build`

This will expose the endpoint: `localhost:8080`.

## The API

This app has 1 endpoint.

### /process/

A post endpoint that receives a json in the body, this json is enqueued in Redis as a parameter of a writer function that will be afterwards get by the consumer service (Redis worker) The json data should be finally added as a new line in the output.txt file in the consumer container.

## Tests

Not implememented yet.
