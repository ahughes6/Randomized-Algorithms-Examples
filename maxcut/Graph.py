# Graph representation using a set of sets.
# Undirected graph using adjacency "lists" (sets).
class Graph:
  def __init__(self, n):
    self.V = set(i for i in range(n))
    self.E = {i : set() for i in range(n)}
    self.num_edges = 0

  def addEdge(self, u, v):
    if v not in self.E[u]: self.num_edges += 1
    self.E[u].add(v)
    self.E[v].add(u)

  def __len__(self):
    return len(self.V)

  def isEdge(self,u,v):
    return v in self.E[u]
