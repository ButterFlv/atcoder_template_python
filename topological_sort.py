from collections import deque
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(V):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans

# main
# --------- 以下にコードを書く ---------

# 頂点を隣接リスト表現
G = []

# 入次数のリスト(入次数：その頂点に入ってくる頂点の数)
into_num = []

# 結果を変数 ans に配列として格納
ans = topological_sort(G, into_num)

#トポロジカルソートされたリストの頂点数　と　元のグラフの頂点数を比較することで DAG かどうか判定
# if len(ans)==len(G):
#     print('閉路なし') #同じ頂点数なら閉路なし
# else:
#     print('閉路有り') #頂点数が異なると閉路が存在している
