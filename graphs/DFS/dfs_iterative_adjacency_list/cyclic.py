from vertex import Vertex
from graph import Graph

railway = Graph()

A = Vertex('A')
B = Vertex('B')
C = Vertex('C')
D = Vertex('D')

railway.add_vertex(A)
railway.add_vertex(B)
railway.add_vertex(D)
railway.add_vertex(C)

railway.add_edge(B, D)
railway.add_edge(D, A)
railway.add_edge(A, B)

B_to_C_path_exists = railway.find_path('B', 'C')
D_to_B_path_exists = railway.find_path('D', 'B')

print("\nA path exists between B and C:")
print(B_to_C_path_exists)
print("\nA path exists between D and B:")
print(D_to_B_path_exists)
