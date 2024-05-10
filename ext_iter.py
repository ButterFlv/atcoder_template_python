class ext_iter:

  @staticmethod
  def permutations(_arr):
    global ___more_more_iter_result
    ___more_more_iter_result = []
    arr, len_ = sorted(_arr), len(_arr)
    def dfs(bit, res):
      if len(res) == len_:
        ___more_more_iter_result.append(tuple(res))
        return
      for i in range(len_):
        if bit&(1<<i) == 0:
          dfs(bit | (1<<i), res + [arr[i]])
    dfs(0, [])
    return iter(___more_more_iter_result)

  @staticmethod
  def duplicate_permutations(_arr):
    global ___more_more_iter_result
    ___more_more_iter_result = []
    arr, len_ = sorted(_arr), len(_arr)
    everMask = dict()
    for i in range(len_):
      if everMask.get(arr[i]) == None:
        everMask[arr[i]] = 1<<i
      else:
        everMask[arr[i]] |= 1<<i
    def dfs(bit, res):
      if len(res) == len_:
        ___more_more_iter_result.append(tuple(res))
        return
      everBit = 0
      for i in range(len_):
        if bit&(1<<i) == 0 and everBit&(everMask[arr[i]]) == 0:
          everBit |= 1<<i
          dfs(bit | (1<<i), res + [arr[i]])
    dfs(0, [])
    return iter(___more_more_iter_result)
