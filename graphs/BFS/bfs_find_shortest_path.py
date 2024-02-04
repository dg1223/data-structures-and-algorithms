from collections import deque

class BFS:
    def __init__(self, graph):
        length = len(graph)
        self.level = {}
        self.parent_array = {}
        self.visited = set()
        self.graph = graph


    def bfs(self, start, target):    
        queue = deque()

        queue.appendleft(start)
        self.visited.add(start)
        self.level[start] = 0

        while queue:
            parent = queue.pop()            
            for child in self.graph[parent]:
                if child not in self.visited:
                    queue.appendleft(child)
                    self.visited.add(child)
                    self.level[child] = self.level[parent] + 1
                    self.parent_array[child] = parent

    def print_shortest_path(self, start, target):
        # run BFS to populate parent_array
        self.bfs(start, target)

        path = []
        while target != start:
            path.append(target)
            target = self.parent_array[target]

        # include the source vertex
        path.append(start)

        path = path[::-1]

        for vertex in path:
            print(vertex)

'''
			A
		/	  	\
	   B     	 C
	 / 	 \     /
	D     E - F
'''

graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

'''
		   Lava
		/	   	 \
	   S     	  P
	 / 	 \      /
	B    Ls -- C
'''

graph_2 = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

shortest_path = BFS(graph_1)
shortest_path.print_shortest_path("A", "F")
print()
shortest_path = BFS(graph_2)
shortest_path.print_shortest_path("crocodiles", "bees")
