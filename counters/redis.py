import time
import re
import redis

class RedisCounters:
  def __init__(self, host='localhost', port=6379, db=0, redis=None, rootkey='counters'):
    self.keyre = re.compile('\A[\w.]+\Z')
    self.rootkey = rootkey

    if redis:
      self.redis = redis
    else:
      self.redis = redis.Redis(host=host, port=port, db=db)

  def ping(self, key):
    self.redis.hset("pings.%s" % key, int(time.time()))
