import redis
import os

def get_redis_connection():
    # Connect to the Redis server in Docker
    r = redis.Redis(host=os.getenv('REDIS_HOST', 'localhost'), port=6379, db=0)
    return r