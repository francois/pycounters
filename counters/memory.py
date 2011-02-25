import time

from counters import BaseCounters

class MemoryCounters(BaseCounters):
  def __init__(self):
    if hasattr(BaseCounters, '__init__'):
      BaseCounters.__init__(self)

    self.pings = {}

  def do_ping(self, key, at):
    self.pings[key] = at
