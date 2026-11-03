class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_n = max(nums)
        ans = 0
        for i in nums:
            ans += max_n - i
        return ans 

        