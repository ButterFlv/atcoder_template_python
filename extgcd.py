# ax+by=±gcd(a, b) となる整数の組(x, y)を計算
# O(log min(|a|, |b|))
# max(|x|, |y|)<=max(|a|, |b|) が保証される
def extgcd(a, b):
  if b == 0: return (1, 0)
  y, x = extgcd(b, a%b)
  y -= a // b * x
  return (x, y)
