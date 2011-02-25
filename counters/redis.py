import redis

from counters import BaseCounters

class RedisCounters(BaseCounters):
  def __init__(self, host='localhost', port=6379, db=0, redis=None, rootkey='counters'):
    if hasattr(BaseCounters, '__init__'):
      BaseCounters.__init__(self)

    self.rootkey = rootkey

    if redis:
      self.redis = redis
    else:
      self.redis = redis.Redis(host=host, port=port, db=db)

  def do_ping(self, key, at):
    self.redis.hset("pings.%s" % key, at)
