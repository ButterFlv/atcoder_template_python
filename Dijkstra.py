import heapq

class edge:
  def __init__(self, _end, _weight):
    self.end = _end
    self.weight = _weight
  def __str__(self):
    return "end: " + str(self.end) + ", weight: " + str(self.weight)

class Dijkstra:
  def __init__(self, _verts, _edges):
    self.V = _verts
    self.E = _edges
    self.done = {v: False for v in self.V}
    self.dist = {v: 1<<60 for v in self.V}
  def exec(self, start):
    queue = []
    self.done = {v: False for v in self.V}
    self.dist = {v: 1<<60 for v in self.V}
    heapq.heappush(queue, (0, start))
    while queue:
      dist, v = heapq.heappop(queue)
      if self.done[v] or dist > self.dist[v]: continue
      self.done[v] = True
      self.dist[v] = dist
      for e in self.E[v]:
        if self.done[e.end]: continue
        new_dist = dist + e.weight
        if new_dist < self.dist[e.end]:
          self.dist[e.end] = new_dist
          heapq.heappush(queue, (new_dist, e.end))
