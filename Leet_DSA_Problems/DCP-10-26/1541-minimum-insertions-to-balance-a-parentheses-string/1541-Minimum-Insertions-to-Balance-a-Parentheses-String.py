class Solution:
    def minInsertions(self, s: str) -> int:
        d = 0
        res = 0
        for i in s:
            if i =='(':
                d += 2
                if d % 2 == 1:
                    res +=1
                    d -=1
            else:
                d -= 1
                if d < 0:
                    res += 1
                    d = 1 
        return res + d 
                
        return d
        