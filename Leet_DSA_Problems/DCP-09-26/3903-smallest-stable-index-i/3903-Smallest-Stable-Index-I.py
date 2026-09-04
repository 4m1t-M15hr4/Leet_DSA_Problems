class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        max_till = nums[0]
        max_left =[]
        
        for i in range(n):
            if nums[i] > max_till:
                max_till = nums[i]
            max_left.append(max_till)
        
        min_till = nums[n -1]
        min_left= []
        for i in range(n-1, -1, -1):
            if nums[i] < min_till:
                min_till = nums[i]
            min_left.append(min_till)

        min_left = min_left[::-1]
        for i in range(n):
            instable = max_left[i] - min_left[i]
            if instable <= k:
                return i 
        return -1
