class mint:
  MOD = 998244353

  def __init__(self, n): self.n = n % self.MOD

  def __str__(self): return str(self.n)
  __repr__ = __str__
  def __int__(self): return self.n

  def __add__(self, other):
    return mint(self.n+other.n)if isinstance(other,mint)else mint(self.n+other)
  def __sub__(self, other_mint):
    return mint(self.n-other.n)if isinstance(other,mint)else mint(self.n-other)
  def __mul__(self, other_mint):
    return mint(self.n*other.n)if isinstance(other,mint)else mint(self.n*other)
  def __truediv__(self, other_mint):
    return mint(self.n*mint.iegcd(other.n))if isinstance(other,mint)else mint(self.n*mint.iegcd(other))
  def __pow__(self, other):
    return mint(pow(self.n, other_number, mint.MOD))

  __radd__ = __add__
  def __rsub__(self, other):
    return mint(other.n-self.n)if isinstance(other,mint)else mint(other-self.n)
  __rmul__ = __mul__
  def __rtruediv__(self, other):
    return mint(other.n*mint.iegcd(self.n))if isinstance(other,mint)else mint(other*mint.iegcd(self.n))

  def __pos__(self): return self
  def __neg__(self): return mint(0 - self.n)

  def __eq__(self, other):
    return self.n == other.n
  def __ne__(self, other):
    return not self.__eq__(other)

  def iegcd(a):
    u = 1; v = 0; b = mint.MOD
    while b:
      t = a // b
      a -= t * b; a, b=b, a
      u -= t * v; u, v=v, u
    return u % mint.MOD
