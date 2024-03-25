import heapq

# 辺情報を表す構造体
class edge:
    def __init__(self, end, leng):
        self.end = end      # 辺の終点
        self.leng = leng    # 辺の重み

INF = 10**18 # 初期化で使う十分大きな数

# main
# 入力を受け取る
N = int(input())

################################################################################

G = [[] for _ in range(N)]  # G[i]：頂点 i を始点とする辺情報を格納する
for i in range(N-1):
    ##### 頂点を配列 G に入れる #################################################
  
    # a,b,x = map(int,input().split())
    # #u, v, w = map(int, input().split())
    # G[i].append(edge(i+1, a))
    # G[i].append(edge(x-1, b))

################################################################################

dist = [INF for _ in range(N)]  # dist[i]：頂点 0 から頂点 i への暫定的な経路長
dist[0] = 0
done = [False for _ in range(N)]    # done[i]：頂点 i の最短距離が確定しているか

hq = [] # (仮の最短距離、頂点番号) を管理するヒープ
heapq.heapify(hq)

# ヒープに最初の時点における情報を入れておく
for v in range(N):
    heapq.heappush(hq, (dist[v], v))

while len(hq) > 0:
    # ヒープの先頭要素を取り出す (v は頂点番号、d は 0 → v の仮の最短距離)
    [d, v] = heapq.heappop(hq)
    # 頂点 v の最短距離がすでに確定しているなら、何もしない
    if done[v]: continue

    # 頂点 v を始点とする辺 e について、更新を行う
    for e in G[v]:
        if dist[e.end] > dist[v] + e.leng:
            # 距離の更新がある場合には、ヒープに更新後の情報を入れる
            dist[e.end] = dist[v] + e.leng
            heapq.heappush(hq, (dist[e.end], e.end))
    # 頂点 v の最短距離を確定させる
    done[v] = True

print(dist[N-1])
