class mint:
  MOD = 998244353

  def __init__(self, n): self.n = n % self.MOD

  def __str__(self): return str(self.n)
  __repr__ = __str__

  def __add__(self, other_mint):
    return mint(self.n + other_mint.n)
  def __sub__(self, other_mint):
    return mint(self.n - other_mint.n)
  def __mul__(self, other_mint):
    return mint(self.n * other_mint.n)
  def __truediv__(self, other_mint):
    return mint(self.n * mint.inv_extgcd(other_mint.n))
  def __pow__(self, other_number):
    return mint(pow(self.n, other_number, mint.MOD))

  def __pos__(self): return self
  def __neg__(self): return mint(0 - self.n)

  def __eq__(self, other):
    return self.n == other.n
  def __ne__(self, other):
    return not self.__eq__(other)

  def inv_extgcd(a):
    u = 1; v = 0; b = mint.MOD
    while b:
      t = a // b
      a -= t * b; a, b=b, a
      u -= t * v; u, v=v, u
    return u % mint.MOD
