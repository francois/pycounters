import unittest
import time

from counters import RedisCounters
from mock import Mock

class FakeRedis:
  pass

class RedisCountersTestCase(unittest.TestCase):
  def setUp(self):
    self.redis_mock = FakeRedis()
    self.counter = RedisCounters(rootkey='counters', redis=self.redis_mock)

  def test_ping_does_an_hset_on_the_root_key(self):
    self.redis_mock.hset = Mock(return_value=1)
    self.counter.ping("a.b")
    self.redis_mock.hset.assert_called_with('pings.a.b', int(time.time()))
