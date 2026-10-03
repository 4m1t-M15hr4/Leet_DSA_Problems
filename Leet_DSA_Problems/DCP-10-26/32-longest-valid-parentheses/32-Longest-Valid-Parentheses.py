class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        def check(s, ov, cv):
            d = 0
            res = 0
            l = 0
            for r in range(n):
                d += ov if s[r] == '(' else cv
                if d < 0:
                    d = 0
                    l =  r + 1
                if d == 0: res = max(res, r - l + 1)
            return res
        return max(check(s, 1, -1), check(s[::-1],-1, 1 )) 


        