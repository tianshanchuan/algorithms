G = {'A': ['B', 'C'],
     'B': ['A', 'D', 'E'],
     'C': ['A', 'F'],
     'D': ['B'],
     'E': ['B', 'F'],
     'F': ['C', 'E']}


def bfs(graph, start):
    """
    >>> ''.join(sorted(bfs(G, 'A')))
    'ABCDEF'
    """
    explored, queue = set(), [start]  # collections.deque([start])
    explored.add(start)
    
    while queue:
        v = queue.pop(0)  # queue.popleft()
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.append(w)
                print(explored, queue)
    return explored


if __name__ == '__main__':
    print(bfs(G, 'A'))




def bfs_self(graph, start):
    explored, queue = set(), [start]
    while queue:
        v = queue.pop(0)
        for v in graph[v]:
            if v not in explored:
                explored.add(v)
                queue.append(v)
    return explored

if __name__ == '__main__':
    print(bfs_self(G, 'A'))