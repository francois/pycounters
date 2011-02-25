#
import unittest
from tests.memory_counters import MemoryCountersTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MemoryCountersTestCase))
    return suite
