from collections import deque  # Untuk queue efisien di BFS

class Graph:
    def __init__(self, V):
        self.V = V  # Jumlah simpul
        self.graph = [[] for _ in range(V)]  # Adjacency list

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Tambah edge u -> v (directed)

    def dfs(self, v, visited):
        # DFS rekursif: tandai kunjungan, cetak, rekursi ke tetangga tak terkunjungi
        visited[v] = True
        print(v, end=" ")
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

    def dfs_iterative(self, start):
        # DFS iteratif: gunakan stack untuk simulasi rekursi
        visited = [False] * self.V
        stack = [start]  # Stack simpan simpul
        visited[start] = True
        while stack:
            current = stack.pop()  # Pop dari akhir (LIFO)
            print(current, end=" ")
            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True  # Tandai saat push hindari duplikat

    def bfs(self, start):
        # BFS: gunakan queue untuk level-order
        visited = [False] * self.V
        queue = deque([start])  # Deque untuk popleft efisien
        visited[start] = True
        while queue:
            current = queue.popleft()  # FIFO
            print(current, end=" ")
            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Contoh penggunaan
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("DFS Rekursif (start 0):")
visited = [False] * 4
g.dfs(0, visited)
print("\nDFS Iteratif (start 0):")
g.dfs_iterative(0)
print("\nBFS (start 0):")
g.bfs(0)
