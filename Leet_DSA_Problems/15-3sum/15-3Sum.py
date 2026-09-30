class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for x in range(n-2):
            if x  > 0 and nums[x] == nums[x - 1]:
                
                continue
            i = x + 1
            j = n - 1
            while i < j:
                total = nums[i] + nums[x] +nums[j]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    res.append([nums[i],nums[j],nums[x]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
        
                    i += 1
                    j -= 1
        return res   

            # [-4,-1,-1,0,1,2]

        