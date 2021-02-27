"""
1   2  3  4
5   6  7  8
9  10  11 12
13 14 15  16
"""
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return matrix;
        start_col=0
        end_col=len(matrix[0])
        start_row=0
        end_row=len(matrix)
        arr=[]
        while(start_row<end_row and start_col<end_col):
            #left
            if start_row<end_row:
                arr.extend([matrix[start_row][i] for i in range(start_col,end_col)])
            start_row+=1
            #down
            if start_col < end_col:
                arr.extend([matrix[i][end_col-1] for i in range(start_row,end_row)])
            end_col-=1
            #left
            if start_row<end_row:
                arr.extend([matrix[end_row-1][i] for i in range(end_col-1,start_col-1,-1)])
            end_row-=1
            #up
            if start_col < end_col:
                arr.extend([matrix[i][start_col] for i in range(end_row-1,start_row-1,-1)])
            start_col+=1
        return arr

s=Solution()
arr1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(s.spiralOrder(arr1))