import random
class RollingHash:
  def __init__(self, BASE=None, MOD=None):
    self.BASE = BASE; self.MOD = MOD
    if self.BASE == None:
      self.BASE = random.randint(1<<50, 1<<60)
    if self.MOD == None:
      self.MOD = (1<<61)-1
    self.B = [1]

  def __calcBPower(self, Length):
    while len(self.B)<Length:
      self.B.append((self.B[-1] * self.BASE) % self.MOD)

  def makeHash(self, String):
    res = [0]; self.__calcBPower(len(String)+9)
    for i in range(len(String)):
      res.append((res[-1]*self.BASE + ord(String[i])) % self.MOD)
    return tuple(res)

  def getHash(self, Hash, L, R):
    return (Hash[R]-Hash[L]*self.B[R-L]) % self.MOD
