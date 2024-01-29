from collections import deque

class BFS:
    def __init__(self, graph):
        length = len(graph)
        self.level = [-1 for _ in range(length)]
        self.parent_array = [-1 for _ in range(length)]
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
        start_index = list(self.graph.keys()).index(start)
        target_index = list(self.graph.keys()).index(target)
        self.bfs(start_index, target_index)

        path = []
        while target != -1:
            path.append(target_index)
            target_index = self.parent_array[target_index]

        path = path[::-1]

        for vertex_index in path:
            vertices = list(self.graph.keys())
            print(vertices[vertex_index])


graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

shortest_path = BFS(graph)
shortest_path.print_shortest_path("crocodiles", "bees")