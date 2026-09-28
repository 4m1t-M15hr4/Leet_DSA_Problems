class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        mx = 0
        for i in s:
            if i =='(':
                cnt += 1
                mx = max(mx, cnt)
            elif i == ')':
                cnt -=1
        return mx