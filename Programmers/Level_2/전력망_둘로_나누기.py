from collections import defaultdict

def get_count(n, board, answer):
    total = set(range(1, n + 1))
    visited = set()
    q = [1]
    while q:
        new = q.pop()
        visited.add(new)

        for i in range(1, n + 1):
            if (i in board[new]) and (i not in visited):
                q.append(i)
    return len(visited)

def solution(n, wires):
    board = defaultdict(list)
    result = []

    for a, b in wires:
        board[a].append(b)
        board[b].append(a)

    for a, b in wires:
        board[a].remove(b)
        board[b].remove(a)
        answer = 0
        answer = get_count(n, board, answer)
        result.append(abs(n - (2 * answer)))
        board[a].append(b)
        board[b].append(a)

    answer = min(result)
    return answer
