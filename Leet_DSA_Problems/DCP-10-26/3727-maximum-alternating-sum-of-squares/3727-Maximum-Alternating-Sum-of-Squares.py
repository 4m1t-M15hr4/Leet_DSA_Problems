class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
        nums.sort()
        n = len(nums)
        m = n // 2
        ans = 0
        for i in range(m):
            ans -= nums[i]
        for i in range(m, n):
            ans += nums[i]
        return ans


    
        