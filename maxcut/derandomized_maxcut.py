# Graph contains n vertices.
def at_least_half_cut(G):
  S = set()
  S.add(0)
  for i in range(1,len(G)):
    # Maximize expectation for the value of i in S.
    i_in_S_expectation = compute_partial_expectation(G,S,i,True)
    i_not_in_S_expectation = compute_partial_expectation(G,S,i,False)
    # If tie, we will also put i into S.
    if i_in_S_expectation >= i_not_in_S_expectation: S.add(i)
  return S

def compute_partial_expectation(G,S,i,i_in_S):
  expected_cut_size = 0
  u = i
  for v in G.E[u]:
    if v < i:
      if (v in S) != i_in_S: expected_cut_size += 1
    else:
      expected_cut_size += 0.5
  return expected_cut_size

