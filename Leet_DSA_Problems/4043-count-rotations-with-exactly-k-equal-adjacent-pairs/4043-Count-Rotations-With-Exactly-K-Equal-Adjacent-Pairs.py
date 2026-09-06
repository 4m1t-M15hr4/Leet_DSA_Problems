class Solution(object):
    def countRotations(self, s, k):
        n = len(s)
        sum = 0
        for i  in range(n):
            if s[i] == s[(i +1 ) % n]:
                sum += 1
        if k == sum-1:
            return sum
        if k == sum:
            return n- sum
        return 0
            
        
        