'''
We use levels to find the shortest distance between two vertices.
'''

from collections import deque

class BFS:
    def __init__(self, graph):
        self.visited = set()
        self.levels = {}
        self.graph = graph

    def bfs(self, start):    
        queue = deque()
        queue.appendleft(start)
        self.visited.add(start)
        self.levels[start] = 0;

        while queue:
            parent = queue.pop()

            for child in self.graph[parent]:
                if child not in self.visited:
                    queue.appendleft(child)
                    self.visited.add(child)
                    self.levels[child] = self.levels[parent]+1

    def print_levels(self, start):
        self.bfs(start)
        for level in self.levels:
            print(f"level of {level} = {self.levels[level]}")


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

shortest_distance = BFS(graph_1)
shortest_distance.print_levels("A")

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

print()
shortest_distance = BFS(graph_2)
shortest_distance.print_levels("lava")
