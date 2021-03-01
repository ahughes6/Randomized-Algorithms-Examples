from Graph import Graph
import randomized_maxcut
import derandomized_maxcut

n = int(input("Enter size n: "))
g = Graph(n)
for i in range(n):
  for j in range(i+1,n):
    g.addEdge(i,j)

#print(g.V,g.E)

#for i in range(5):
#  S = randomized_maxcut.approx_max_cut(g)
#  print(S,randomized_maxcut.compute_cut_size(g,S))

#S = randomized_maxcut.approx_max_cut_w_exp(g)
#print(S,randomized_maxcut.compute_cut_size(g,S))

S = derandomized_maxcut.at_least_half_cut(g)
print(S,randomized_maxcut.compute_cut_size(g,S))

g = Graph(n)
for i in range(0,int(n/2)):
  for j in range(int(n/2),n):
    g.addEdge(i,j)

S = derandomized_maxcut.at_least_half_cut(g)
print(S,randomized_maxcut.compute_cut_size(g,S))

g = Graph(n)
import random
vertices = [i for i in range(n)]
#random.shuffle(vertices)
for i in range(0,int(n/4)):
  for j in range(int(n/4),n):
    g.addEdge(vertices[i],vertices[j])

for i in range(0,int(n/4)-2):
  g.addEdge(i,i+1)
  g.addEdge(i,i+2)
for j in range(int(n/4),n-2):
  g.addEdge(i,i+1)
  g.addEdge(i,i+2)

S = derandomized_maxcut.at_least_half_cut(g)
print(S,randomized_maxcut.compute_cut_size(g,S))
