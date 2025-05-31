# Method- 1 (Using DFS)
def numIslands(grid):
    if not grid:
        return 0
    def dfs(grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark the cell as visited
        dfs(grid, i + 1, j)  # Move down
        dfs(grid, i - 1, j)  # Move up
        dfs(grid, i, j + 1)  # Move right
        dfs(grid, i, j - 1)  # Move left

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count
# Example usage:
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# print(numIslands(grid))  # Output: 3


# Method - 2 (Using BFS)
# from collections import deque
# m, n = len(grid), len(grid[0])
# dirs = [(1,0),(-1,0),(0,1),(0,-1)]
# islands = 0
# for i in range(m):
#     for j in range(n):
#         if grid[i][j] == '1':
#             islands += 1
#             # mark and explore this island
#             grid[i][j] = '0'
#             q = deque([(i, j)])
#             while q:
#                 x, y = q.popleft()
#                 for dx, dy in dirs:
#                     nx, ny = x + dx, y + dy
#                     if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
#                         grid[nx][ny] = '0'
#                         q.append((nx, ny))








# Example 2 (Using BFS to find the time taken for all oranges to rot)
from collections import deque
def orangesRotting(mat):
    rows , cols = len(mat) , len(mat[0])
    queue = deque([])
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 2:
                queue.append((r,c,0))
            if mat[r][c] == 1:
                fresh += 1     
    directions = [(0,1), (1,0), (0,-1), (-1,0)]      
    time = 0
    while queue:
        r, c , t = queue.popleft()
        time = max(time,t)
        for dr,dc in directions:
            nr , nc = r + dr , c + dc
            if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == 1:
                mat[nr][nc] = 2
                fresh -= 1
                queue.append((nr,nc,t+1)) 
    return time if fresh == 0 else -1



# Method - 2 (Using DFS to find the time taken for all oranges to rot)

def orangesRotting(mat):
    rows, cols = len(mat), len(mat[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    time = 0
    fresh = sum(row.count(1) for row in mat)
    def dfs(r, c, t):
        nonlocal time
        if r < 0 or r >= rows or c < 0 or c >= cols or mat[r][c] != 1:
            return
        mat[r][c] = 2  # Mark the orange as rotten
        fresh -= 1
        time = max(time, t)
        for dr, dc in directions:
            dfs(r + dr, c + dc, t + 1)
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 2:
                dfs(r, c, 0)
    return time if fresh == 0 else -1
# Example usage:
# mat = [
#     [2, 1, 1],
#     [1, 1, 0],
#     [0, 1, 1]
# ]
