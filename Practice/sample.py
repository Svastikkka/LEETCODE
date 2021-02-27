class Solution:
    def numIslands(self, grid) -> int:
        numOfIslands=0
        if len(grid)==0:
            return 0
        for i in range(0,len(grid)):
            for j in  range(0,len(grid)):
                if grid[i][j]=="1":
                    numOfIslands=self.dfs(grid,i,j)
        return numOfIslands
    def dfs(self,grid,i,j):
        if i<0 or i >=len(grid) or j<0 or j>=len(grid) or grid[i][j]=="0":
            return 0
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        return 1
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
s=Solution()
print(s.numIslands(grid))