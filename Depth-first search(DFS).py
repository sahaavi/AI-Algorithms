from collections import defaultdict
from collections import deque


class Graph():
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        if self.directed:
            self.graph[u].append(v)
        else:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def dfs(self, vertex):
        visited = []
        stack = deque()
        stack.append(vertex)

        while len(stack) != 0:
            vertex = stack.pop()
            if vertex in visited:
                continue
            print(vertex, end=" ")
            visited.append(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)


g = Graph(True)

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'D')
g.add_edge('D', 'F')

g.dfs('A')
