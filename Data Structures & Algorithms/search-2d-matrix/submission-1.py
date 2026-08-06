class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix),len(matrix[0])
        l,r = 0,ROWS*COLS-1
        while (l<=r):
            m = l +((r-l)//2)
            rows = m//COLS
            cols = m%COLS
            if target>matrix[rows][cols]:
                l=m+1
            elif target<matrix[rows][cols]:
                r=m-1
            else:
                return True
        return False