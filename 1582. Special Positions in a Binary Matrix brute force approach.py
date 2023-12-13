class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        total=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    count+=1
                    a=0
                    b=0
                    while(b<len(mat[0])):
                        if mat[i][b]==1 and b!=j:
                            count+=1
                        b+=1
                    while(a<len(mat)):
                        if mat[a][j]==1 and a!=i:
                            count+=1
                        a+=1
                if count==1:
                    total+=1
                count=0
        return total
"""insted of while we can use for loop to it reduse the time complaxity too"""
