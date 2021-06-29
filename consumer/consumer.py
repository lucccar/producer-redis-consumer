    """This file is the redis worker that will set up the connection with redis, 
        get the enqueued jobs and call the function to write the txtfile.
    """

import redis
from rq import Worker, Queue, Connection

from producer.constants import redis_url

listen = ['default']

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
