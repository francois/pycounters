import redis
from counters import BaseCounters

class RedisCounters(BaseCounters):
  def __init__(self, redis_instance=None, rootkey='counters'):
    if hasattr(BaseCounters, '__init__'):
      BaseCounters.__init__(self)

    self.rootkey = rootkey

    if redis_instance:
      self.redis = redis_instance
    else:
      self.redis = redis.Redis(host='localhost', port=6379, db=0)

  def do_hit(self, key, n):
    self.redis.hincrby(self.rootkey, "hits.%s" % key, n)

  def do_ping(self, key, at):
    self.redis.hset(self.rootkey, "pings.%s" % key, at)
