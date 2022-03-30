# CSE 531 (Fall 2022) Programming Assignment 1
from collections import defaultdict


def countComponents(n, edges):
    def dfs(node, c):
        # DFS to check visited components
        for e in adj[node]:
            if e not in visited:
                visited.add(e)
                c = dfs(e, c + 1)
        return c

    # Creating the adjacency list
    adj = defaultdict(list)
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    # Hashmap to track vertices visited
    visited = set()

    # Initialising counts
    numConn = 0
    maxLen = 0

    # Looping to get number of connected components
    for node in range(1, n + 1):
        if node not in visited:
            visited.add(node)
            numConn += 1
            c = dfs(node, 1)
            maxLen = max(maxLen, c)

    print(numConn)
    print(maxLen)


# Input
n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append([a, b])

# Calling the function
countComponents(n, edges)
