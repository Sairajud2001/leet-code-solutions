class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        g=len(grid)
        t=len(grid[0])
        r={}
        c={}
        m=[[i for i in range(len(grid[0]))]for i in range(len(grid))]
        for i in range(len(grid)):
            row_sum=0
            for j in range(len(grid[0])):
                row_sum+=grid[i][j]
            r[i]=row_sum
           # print(row_sum,i)
        for j in range(t):
            col_sum=0
            for i in range(g):
                col_sum+=grid[i][j]
            c[j]=col_sum
            #print(col_sum,j)
        for i in range(g):
            for j in range(t):
                m[i][j]=r[i]+c[j]-(g-r[i])-(t-c[j])
        return m
        
                
        
                             
            
        
