from collections import deque

N = 8


# check if queen placement is safe
def is_safe(board, row, col):
    for r in range(row):
        c = board[r]

        # same column
        if c == col:
            return False

        # diagonal check
        if abs(c - col) == abs(r - row):
            return False

    return True


# ---------------- DFS ----------------
def dfs(row, board):
    if row == N:
        print("DFS Solution:", board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            dfs(row + 1, board)
            board[row] = -1   # backtrack


# ---------------- BFS ----------------
def bfs():
    queue = deque()
    queue.append((0, []))  # (row, board configuration)

    while queue:
        row, board = queue.popleft()

        if row == N:
            print("BFS Solution:", board)
            continue

        for col in range(N):
            if is_safe(board, row, col):
                queue.append((row + 1, board + [col]))


# ---------------- MAIN ----------------
print("DFS Results:")
board = [-1] * N
dfs(0, board)

print("\nBFS Results:")
bfs()
