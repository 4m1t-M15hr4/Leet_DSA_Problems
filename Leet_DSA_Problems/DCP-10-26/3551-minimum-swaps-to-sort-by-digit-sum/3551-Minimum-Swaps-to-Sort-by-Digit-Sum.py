class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)

        def digit_sum(num: int) -> int:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        target = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps