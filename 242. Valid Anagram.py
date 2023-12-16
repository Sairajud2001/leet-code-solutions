class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m={}
        n={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]]=0

            m[s[i]]+=1
            if t[i] not in n:
                n[t[i]]=0
            
            n[t[i]]+=1
        return m==n
