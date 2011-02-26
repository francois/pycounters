import re
import time

class BaseCounters:
  def __init__(self):
    self.keyre = re.compile('\A[\w.]+\Z')

  def ping(self, key):
    self.validate_key(key)
    self.do_ping(key, int(time.time()))

  def hit(self, key, n=1):
    self.validate_key(key)
    self.do_hit(key, n)

  def validate_key(self, key):
    if re.match(self.keyre, key):
      pass
    else:
      raise ValueError("Counters keys must only contain letters, numbers, the underscore (_) and fullstop (.), received \"%s\"" % key)
