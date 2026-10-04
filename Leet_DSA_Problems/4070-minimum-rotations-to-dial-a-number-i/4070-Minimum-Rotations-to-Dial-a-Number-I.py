class Solution:
    def minRotations(self, s: str) -> int:
        curr = 0
        total = 0
        for c in s:
            target = int(c)
            diff = abs(curr - target)
            total += min(diff, 10 - diff)
            curr = target
        return total