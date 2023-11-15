from vertex import Vertex
from graph import Graph

no_path_exists = True

directed_railway = Graph(True)

station_A = Vertex("A")
station_B = Vertex("B")
station_C = Vertex("C")
station_D = Vertex('D')

directed_railway.add_vertex(station_A)
directed_railway.add_vertex(station_B)
directed_railway.add_vertex(station_D)
directed_railway.add_vertex(station_C)

directed_railway.add_edge(station_D, station_B)
directed_railway.add_edge(station_B, station_A)

path_exists = directed_railway.find_path("D", "D")
print(path_exists)

print("\n\n\nFinding path from D to A\n")
new_path_exists = directed_railway.find_path('D', 'A')
print(new_path_exists)
print("\n\nTrying to find path from D to C\n")
no_path_exists = directed_railway.find_path('D', 'C')
print(no_path_exists)