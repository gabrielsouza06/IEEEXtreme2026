import sys
import heapq
from collections import deque, defaultdict
import math

# 1. HELPER / FAST I/O
input_data = sys.stdin.read().split()
iterator = iter(input_data)

def get_word():
    try:
        return next(iterator)
    except StopIteration:
        return None

def get_number():
    data = get_word()
    if data is None:
        return None
    try:
        return int(data)
    except ValueError:
        return float(data)

# 2. GRAFOS: DIJKSTRA
def dijkstra(start_node, num_nodes, adj_list):
    distances = {i: float('inf') for i in range(num_nodes + 1)}
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > distances[u]:
            continue
        for neighbor, weight in adj_list[u]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

# 3. ESTRUTURA DE DADOS: DSU (Union-Find)
class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            return True
        return False

# 4. MATEMÁTICA: CRIVO DE ERATÓSTENES
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime
