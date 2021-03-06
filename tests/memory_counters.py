import unittest
import time

from counters import MemoryCounters

class MemoryCountersTestCase(unittest.TestCase):
  def setUp(self):
    self.counter = MemoryCounters()

  def test_ping_records_current_time(self):
    self.counter.ping("a.b")
    self.assertEquals(int(time.time()), self.counter.pings["a.b"])

  def test_ping_raises_exception_when_invalid_key(self):
    self.assertRaises(ValueError, self.counter.ping, "a/b")
