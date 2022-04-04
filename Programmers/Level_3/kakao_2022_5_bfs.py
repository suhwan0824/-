from collections import deque
import copy

SHEEP = 0
WOLF = 1

def bfs(info, graph):
    global SHEEP, WOLF

    maxSheep = 0
    q = deque()
    visited_set = set()

    q.append((0, 1, 0, [0]))
    visited_set.add((0, 1, 0))

    while q:
        node, sheep, wolf, visited = q.popleft()
        maxSheep = max(maxSheep, sheep)

        for next_node in graph[node]:
            next_sheep = sheep
            if next_node not in visited and info[next_node] == SHEEP:
                next_sheep += 1

            next_wolf = wolf
            if next_node not in visited and info[next_node] == WOLF:
                next_wolf += 1

            if next_sheep <= next_wolf:
                continue

            next_state = (next_node, next_sheep, next_wolf)

            if next_state not in visited_set:
                visited_set.add(next_state)
                copy_visited = copy.deepcopy(visited)
                copy_visited.append(next_node)

                q.append((next_node, next_sheep, next_wolf, copy_visited))
    return maxSheep

def solution(info, edges):
    graph = dict()
    for i in range(len(edges)):
        graph[i] = []

    for i in range(len(edges)):
        u, v = edges[i]
        graph[u].append(v)
        graph[v].append(u)
    return bfs(info, graph)
