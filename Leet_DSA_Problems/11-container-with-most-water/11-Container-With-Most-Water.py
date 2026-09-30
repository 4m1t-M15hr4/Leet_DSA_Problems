class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = []
        n = len(height)
        i = 0
        j = n-1
        while i < j and n != 0:
            if height[i] <= height[j]:
                res.append((j-i) * height[i])
                i += 1
            elif height[i] > height[j]:
                res.append((j -i)* height[j])
                j -= 1
            n -= 1
                
            # sm = height[i] * height[j]
            # res.append(sm)
            # i +=1
            # j -=1
        return max(res)



        