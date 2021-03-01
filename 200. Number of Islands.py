def numIslands(grid)->int:
    if len(grid) == 0 or not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                count += dfs(grid, i, j)
    return count


def dfs(grid, i, j):
    #base condition for boundries
    if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0'):
        return 0
    grid[i][j] = '0'
    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)
    return 1

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))