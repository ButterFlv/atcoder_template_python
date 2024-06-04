# _size: 操作を行う要素の集合のサイズ (各値は i (0 <= i < _size))
# _f: 集合から集合の写像 (i (0 <= i < _size) に対して定義される)
# _repeat: 操作を行う回数
# dp[i][j]: 要素 j から 2^i 回遷移した要素
def doubling(_size, _f, _repeat):
  _times = 1
  while 2 ** (_times - 1) <= _repeat: _times += 1
  _dp=[[None for __ in range(_size)] for _ in range(_times)]
  for _j in range(_size):
    _dp[0][_j] = _f(_j)
  for _i in range(1, _times):
    for _j in range(_size):
      _dp[_i][_j] = _dp[_i-1][_dp[_i-1][_j]]
  return _dp
