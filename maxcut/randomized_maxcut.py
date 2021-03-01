import secrets

# Graph contains n vertices.
def approx_max_cut(G):
  S = set()
  for i in range(len(G)):
    if secrets.randbelow(2) == 1: S.add(i)
  return S

def approx_max_cut_w_exp(G):
  max_S = set()
  max_cut_size = -1
  for i in range(G.num_edges+2):
    S = approx_max_cut(G)
    cut_size = compute_cut_size(G,S)
    if cut_size > max_cut_size:
      max_cut_size = cut_size
      max_S = S
  return max_S

def compute_cut_size(G,S):
  cut_size = 0
  for u in S:
    for v in G.V - S:
       if G.isEdge(u,v): cut_size += 1
  return cut_size

