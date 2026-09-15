class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

      
        ispali = [[False] * n for _ in range(n)]

        for l in range(1, n + 1):
            for left in range(n - l + 1):
                right = left + l - 1

                ispali[left][right] = (
                    s[left] == s[right] and
                    (l <= 2 or ispali[left + 1][right - 1])
                )

        dp = [0] * n

        for i in range(n):
    
            if i > 0:
                dp[i] = dp[i - 1]

      
            for j in range(i - k + 2):
                if ispali[j][i]:
                    prev = dp[j - 1] if j > 0 else 0
                    dp[i] = max(dp[i], prev + 1)

        return dp[n - 1]