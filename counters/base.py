import re
import time

class BaseCounters:
  def __init__(self):
    self.keyre = re.compile('\A[\w.]+\Z')

  def ping(self, key):
    self.validate(key)
    self.do_ping(key, int(time.time()))

  def validate(self, key):
    if re.match(self.keyre, key):
      pass
    else:
      raise ValueError("Counters keys must only contain letters, numbers, the underscore (_) and fullstop (.), received \"%s\"" % key)
