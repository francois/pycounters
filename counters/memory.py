import time
import re

class InvalidKeyException(ValueError):
  pass

class MemoryCounters:
  def __init__(self):
    self.pings = {}
    self.keyre = re.compile('\A[\w.]+\Z')

  def ping(self, key):
    if re.match(self.keyre, key):
      self.pings[key] = time.time()
    else:
      raise InvalidKeyException("Counters keys must only contain letters, numbers, the underscore (_) and fullstop (.), received \"%s\"" % key)
