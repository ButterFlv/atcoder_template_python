class mint:
  inv = None
  MOD = None

  def init(MOD = 998244353, inv_generate = 1):
    mint.MOD = MOD
    mint.inv = [None]*(inv_generate + 1)
    mint.inv[1] = 1
    for a in range(2, inv_generate + 1):
      mint.inv[a] = ( -(MOD//a) * mint.inv[MOD%a] ) % MOD

  def __init__(self, n): self.n = n % self.MOD

  def __str__(self): return str(self.n)
  __repr__ = __str__

  def __add__(self, other):
    return mint(self.n + other.n) if isinstance(other, mint) else mint(self.n + other)
  def __sub__(self, other):
    return mint(self.n - other.n) if isinstance(other, mint) else mint(self.n - other)
  def __mul__(self, other):
    return mint(self.n * other.n) if isinstance(other, mint) else mint(self.n * other)
  def __truediv__(self, other):
    a, b = self.n, other.n if isinstance(other, mint) else other % self.MOD
    return mint(a * self.inv[b]) if b<len(self.inv) else mint(a * self.inv_extgcd(b))
  def __pow__(self, other):
    return mint(pow(self.n, other.n, self.MOD)) if isinstance(other, mint) else mint(pow(self.n, other, self.MOD))

  __radd__ = __add__
  def __rsub__(self, other):
    return mint(other.n - self.n) if isinstance(other, mint) else mint(other - self.n)
  __rmul__ = __mul__
  def __rtruediv__(self, other):
    a, b = other.n if isinstance(other, mint) else other, self.n
    return mint(a * self.inv[b]) if b<len(self.inv) else mint(a * self.inv_extgcd(b))
  def __rpow__(self, other):
    return mint(pow(other.n, self.n, self.MOD)) if isinstance(other, mint) else mint(pow(other, self.n, self.MOD))

  def __pos__(self): return self
  def __neg__(self): return 0-self

  def __eq__(self, other):
    return self.n == other.n if isinstance(other, mint) else self.n == other%self.MOD
  def __ne__(self, other):
    return not self.__eq__(other)

  def inv_extgcd(a):
    u = 1; v = 0; b = MOD
    while b:
      t = a // b
      a -= t * b; a, b=b, a
      u -= t * v; u, v=v, u
    return u % MOD
