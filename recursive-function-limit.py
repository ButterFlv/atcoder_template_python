# 再帰関数を書くときは CPython に設定
# ↑ これをしないと TLE や MLE になる

# 再帰関数の処理回数の上限を設定する
import sys

sys.setrecursionlimit(1000_000)

# メモ化再帰をするときの処理 @lru_cache(maxsize=None) を関数宣言の上につける
from functools import lru_cache

@lru_cache(maxsize=None)
