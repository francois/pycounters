import unittest
import time

from counters.memory import MemoryCounters, InvalidKeyException

class MemoryCountersTestCase(unittest.TestCase):
  def setUp(self):
    self.counter = MemoryCounters()

  def test_ping_records_current_time(self):
    self.counter.ping("a.b")
    now = time.time()
    self.assertAlmostEquals(now, self.counter.pings["a.b"], 0.01)

  def test_ping_raises_exception_when_invalid_key(self):
    self.assertRaises(InvalidKeyException, self.counter.ping, "a/b")