def n_ary_k_digits(_n, _k):
  return [[(_i//pow(_n, _j))%_n for _j in range(_k)] for _i in range(pow(_n, _k))]
