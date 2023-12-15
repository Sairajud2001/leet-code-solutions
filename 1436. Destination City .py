class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d={}
        for i in range(len(paths)):
            for j in range(len(paths[0])):
                if paths[i][j] not in d:
                    d[paths[i][j]]=1
                else:
                    d[paths[i][j]]+=1
        for j in range(len(paths)-1,-1,-1):
            if d[paths[j][-1]]==1:
                return paths[j][-1]

        
