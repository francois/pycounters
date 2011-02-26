import unittest
import time

from counters import RedisCounters
from mock import Mock

class FakeRedis:
  pass

class RedisCountersTestCase(unittest.TestCase):
  def setUp(self):
    self.redis_mock = FakeRedis()
    self.counter = RedisCounters(rootkey='counters', redis_instance=self.redis_mock)

  def test_ping_does_an_hset_on_the_root_key(self):
    self.redis_mock.hset = Mock(return_value=1)
    self.counter.ping("a.b")
    self.redis_mock.hset.assert_called_with('counters', 'pings.a.b', int(time.time()))

  def test_ping_raises_exception_when_invalid_key(self):
    self.redis_mock.hset = Mock(return_value=1)
    self.assertRaises(ValueError, self.counter.ping, "a/b")

  def test_hit_with_increment_does_an_hincr_on_the_named_key(self):
    self.redis_mock.hincrby = Mock(return_value=1)
    self.counter.hit('bytes_in', 2019)
    self.redis_mock.hincrby.assert_called_with('counters', 'hits.bytes_in', 2019)

  def test_hit_does_an_hincr_on_the_named_key(self):
    self.redis_mock.hincrby = Mock(return_value=1)
    self.counter.hit('pages_crawled')
    self.redis_mock.hincrby.assert_called_with('counters', 'hits.pages_crawled', 1)
