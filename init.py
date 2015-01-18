#!/usr/bin/env python

from db_redis import redis_conn as redis

auth_token = '205828171.dc1c6fb.8e8366a8dc2c4306945f4a15c89d6e4d'

redis.set('token', auth_token)
