#
import unittest
from tests.memory_counters import MemoryCountersTestCase
from tests.redis_counters import RedisCountersTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MemoryCountersTestCase))
    suite.addTest(unittest.makeSuite(RedisCountersTestCase))
    return suite
