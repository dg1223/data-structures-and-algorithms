'''
We use levels to find the shortest distance between two vertices.
'''

from collections import deque

class BFS:
    def __init__(self, graph):
        self.visited = set()
        self.graph = graph


    def bfs(self, start, target):    
        queue = deque()
		# level of starting vertex is 0
        queue.appendleft((start, 0))
        self.visited.add(start)
        target_found = False;

        while queue:
            parent, level = queue.pop()

            if parent == target:
                print(f"shortest distance = {level}")
                target_found = True

            for child in self.graph[parent]:
                if child not in self.visited:
                    queue.appendleft((child, level+1))
                    self.visited.add(child)

        if not target_found:
            print("Target not found!")


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
shortest_distance.bfs("A", "F")

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
shortest_distance.bfs("crocodiles", "bees")
