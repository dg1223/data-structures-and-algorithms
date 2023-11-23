from vertex import Vertex
from graph import Graph

railway = Graph()

A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')
E = Vertex('E')
F = Vertex('F')
G = Vertex('G')

railway.add_vertex(A)
railway.add_vertex(B)
railway.add_vertex(C)
railway.add_vertex(D)
railway.add_vertex(E)
railway.add_vertex(F)
railway.add_vertex(G)

railway.add_edge(A, B)
railway.add_edge(A, C)
railway.add_edge(B, D)
railway.add_edge(B, E)
railway.add_edge(C, F)
railway.add_edge(C, G)

#B_to_C_path_exists = railway.find_path('B', 'C')
path = railway.find_path('A', 'D')

#print("\nA path exists between B and C:")
#print(B_to_C_path_exists)
print(path)
