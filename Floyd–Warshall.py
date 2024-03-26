# ワーシャルフロイド法を Python で構築

INF = 1<<60 # 初期化で用いる大きな数

# main
# 頂点の数を受け取る
N =

# 隣接行列で表現
V = [[None [] for __ in range(N)] for _ in range(N)]

# 隣接行列表現 V[i][j] : i から j への道があればそのコスト. なければ None ##########

# --------- ここにコードを書く ---------

################################################################################

# 初期化
dist = [[INF for __ in range(N)] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if V[i][j] != None:
      dist[i][j] = V[i][j]

# 本計算
for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# dist[begin][end] で begin から end までの最短距離を求められる ###################

# --------- ここにコードを書く ---------

################################################################################
