import copy

class CumulativeTwoDim:
  def __init__(self, _arr):
    # 幅などをメモ
    self.H, self.W = len(_arr), len(_arr[0])
    # 累積和の配列
    self.cum = copy.deepcopy(_arr)
    # 二方向に累積和をとって二次元をつくる
    for h in range(self.H):
      for w in range(1, self.W):
        self.cum[h][w] += self.cum[h][w-1]
    for w in range(self.W):
      for h in range(1, self.H):
        self.cum[h][w] += self.cum[h-1][w]

  # 0 <= h < H1 かつ 0 <= w < W1 を満たす (h, w) についての和
  # ※　半開区間
  def sum0(self, H1, W1):
    H, W = self.H, self.W
    res = 0
    res += self.cum[H-1][W-1] * (H1//H) * (W1//W)
    res += (self.cum[H1%H-1][W-1] * (W1//W) if H1%H!=0 else 0)
    res += (self.cum[H-1][W1%W-1] * (H1//H) if W1%W!=0 else 0)
    res += (self.cum[H1%H-1][W1%W-1] if H1%H!=0 and W1%W!=0 else 0)
    return res

  # H1 <= h < H2 かつ W1 <= w < W2 を満たす (h, w) についての和
  def sum(self, H1, W1, H2, W2):
    g = self.sum0
    return g(H2, W2) - g(H2, W1) - g(H1, W2) + g(H1, W1)

  def __str__(self):
    StringArr = []
    for h in range(self.H):
      StringArr.append(" ".join(map(str, self.cum[h])))
      StringArr.append("\n")
    return "".join(StringArr)[:-1]
