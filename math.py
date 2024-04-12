################################################################################

# 長さ N の一次元配列において [0,i] (0<=i<N) の区間における要素の総和を
# i 番目に格納した配列を返す
def make_stuck_one_dim(_arr):
  _res, _temp=[], 0
  for _elm in _arr:
    _temp+=_elm
    _res.append(_temp)
  return _res

# スタックを渡してもとの配列の i∊[a,b] なるi番目の要素の総和を計算する
def get_stuck_one_dim(_stuck, _a, _b):
  return (_stuck[_b]-(_stuck[_a-1] if _a>0 else 0))

# 長さ W の配列を H 個格納した配列において a∊[0,i] b∊[0,j] をみたす
# (配列名)[a][b] の総和を [i][j] 番目に格納した配列を返す

def make_stuck_two_dim(_arr, _h, _w):
  _res=[]
  for _i in range(_h):
    _res.append([])
    _stuck=make_stuck_one_dim(_arr[_i])
    for _j in range(_w):
      _res[_i].append(_stuck[_j]+(_res[_i-1][_j] if _i>0 else 0))
  return _res

# スタックを渡してもとの配列の i∊[a,c] j∊[b,d] なる
# [i][j] なる要素の総和を計算する
def get_stuck_two_dim(_stuck, _a, _b, _c, _d):
  return (_stuck[_c][_d]
          -(_stuck[_a-1][_d] if _a>0 else 0)
          -(_stuck[_c][_b-1] if _b>0 else 0)
          +(_stuck[_a-1][_b-1] if (_a>0)and(_b>0) else 0))

# 階乗 n!
def fac(_n):
  res=1
  for i in range(1, _n+1):
    res*=i
  return res

# 順列の nPr
def P(_n, _r):
  res=1
  for i in range(_r):
    res*=(_n-i)
  return res

# 組み合わせのコンビネーション
def C(_n, _r):
  res=1
  _r=(_r if (_n-_r)>_r else _n-_r)
  return P(_n, _r)//fac(_r)

# 平方数判定
def isSquare(_n):
  if _n==0:
    return True
  _left, _right=0, 10**len(str(_n))
  _midi=(_left+_right)//2
  while _left<=_right:
    if _n==_midi**2:
      return True
    if _n<_midi**2:
      _right=_midi-1
    else:
      _left=_midi+1
    _midi=(_right+_left)//2
  return False

# 高速素数判定
import random
def Miller_Rabin_fast(n, k):
  if n==2: return "prime"
  if n%2==0: return "composite"
  s, d=0, n-1
  while d%2==0:
    s, d=s+1, d//2
  if n<4759123141:
    test=(2,7,61)
    for a in test:
      if a>n-1: continue
      check=[]
      check.append(pow(a, d, n)==1)
      for r in range(s):
        check.append(pow(a, pow(2, r)*d, n)==n-1)
      if True in check:
        continue
      else:
        return "composite"
    return "prime"
  elif n<=pow(2, 64):
    test=(2,325,9375,28178,450775,9780504,1795265022)
    for a in test:
      if a>n-1: continue
      check=[]
      check.append(pow(a, d, n)==1)
      for r in range(s):
        check.append(pow(a, pow(2, r)*d, n)==n-1)
      if True in check:
        continue
      else:
        return "composite"
    return "prime"
  else:
    for _ in range(k):
      a=random.randint(1, n-1)
      check=[]
      check.append(pow(a, d, n)==1)
      for r in range(s):
        check.append(pow(a, pow(2, r)*d, n)==n-1)
      if True in check:
        continue
      else:
        return "composite"
    return "probably_prime"

################################################################################
