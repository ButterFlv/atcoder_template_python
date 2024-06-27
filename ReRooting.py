def ReRooting(merge, addroot, e, edge, startvertex = 0):
  import sys
  sys.setrecursionlimit(1000_000)

  dp = [[None for _ in elm]for elm in edge]
  ans = [None]*len(edge)

  def preorder(par, v):
    result = e
    for i in range(len(edge[v])):
      nv = edge[v][i]
      if nv==par: continue
      dp[v][i] = preorder(v, nv)
      result = merge(result, dp[v][i])
    return addroot(result)
  preorder(None, startvertex)

  def postorder(par, dp_par, ce):
    if par==None:
      v = startvertex
    else:
      v = edge[par][ce]
      for i in range(len(edge[v])):
        if edge[v][i]==par: dp[v][i] = dp_par
    L = len(edge[v])
    acc_l = [e]*(L+1); acc_r = [e]*(L+1)
    for i in range(L):
      acc_l[i+1] = merge(acc_l[i], dp[v][i])
    for i in range(L-1, -1, -1):
      acc_r[i] = merge(acc_r[i+1], dp[v][i])
    ans[v] = addroot(acc_l[L])
    for i in range(L):
      nv = edge[v][i]
      if nv==par: continue
      postorder(v, addroot(merge(acc_l[i], acc_r[i+1])), i)
  postorder(None, None, None)

  return ans
