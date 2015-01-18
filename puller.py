#!/usr/bin/env python3

from instagram.client import InstagramAPI
from db_redis import redis_conn as redis

print(redis.get('token'))
