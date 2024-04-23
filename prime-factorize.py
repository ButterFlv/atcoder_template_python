# 素因数分解し、{素因数: 指数} の形の辞書を返す関数
def prime_factorize(n):
  if n <= 1: print("素因数分解できません"); exit()
  obj = dict(); temp = n
  ng = 0; ok = n
  while ok - ng > 1:
    mid = (ok + ng) // 2
    if mid*mid > n: ok = mid
    else: ng = mid
  sqrt_n = ok
  for i in range(2, sqrt_n+1):
    if temp%i != 0: continue
    count = 0
    while temp%i == 0:
      count += 1
      temp //= i
    obj[i] = count
  if temp!=1: obj[temp]=1
  return obj
