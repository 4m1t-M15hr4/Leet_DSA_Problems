class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] *(n +1) for _ in range(n +1)]

        for i in range(n +1):
            comb[i][0] = 1
            comb[i][i] = 1

            for j in range(1, i):
                comb[i][j] = (
                    comb[i -1][j -1] + comb[i -1][j]
                ) % MOD
        
        def dfs(arr):
            if len(arr) <= 1:
                return 1
            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            L = len(left)
            R = len(right)

            interleavings = comb[ L + R][L]

            left_ways = dfs(left)
            right_ways = dfs(right)

            return (
                interleavings * left_ways * right_ways
            ) % MOD
        
        return (dfs(nums)-1) % MOD