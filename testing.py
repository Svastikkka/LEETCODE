def maxgrid(grid, K):
    # N size of rows and M size of cols
    n = len(grid)
    m = len(grid[0])
 
    # To store the prefix sum of matrix
    sum = [[0 for i in range(m + 1)] for j in range(n + 1)]
 
    # Create Prefix Sum
    for i in range(n + 1):
 
        # Traverse each rows
        for j in range(m+1):
            if (i == 0 or j == 0):
                sum[i][j] = 0
                continue
 
            # Update the prefix sum
            # till index i x j
            sum[i][j] = grid[i - 1][j - 1] + sum[i - 1][j] + \
                sum[i][j - 1]-sum[i - 1][j - 1]
 
    # To store the maximum size of
    # matrix with sum <= K
    ans = 0
 
    # Traverse the sum matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
 
            # Index out of bound
            if (i + ans - 1 > n or j + ans - 1 > m):
                break
 
            mid = ans
            lo = ans
 
            # Maximum possible size
            # of matrix
            hi = min(n - i + 1, m - j + 1)
 
            # Binary Search
            while (lo < hi):
 
                # Find middle index
                mid = (hi + lo + 1) // 2
 
                # Check whether sum <= K
                # or not
                # If Yes check for other
                # half of the search
                if (sum[i + mid - 1][j + mid - 1] +
                    sum[i - 1][j - 1] -
                    sum[i + mid - 1][j - 1] -
                        sum[i - 1][j + mid - 1] <= K):
                    lo = mid
 
                # Else check it in first
                # half
                else:
                    hi = mid - 1
 
            # Update the maximum size matrix
            ans = max(ans, lo)
    return ans

print(maxgrid([[4,5],[6,7]], 2))