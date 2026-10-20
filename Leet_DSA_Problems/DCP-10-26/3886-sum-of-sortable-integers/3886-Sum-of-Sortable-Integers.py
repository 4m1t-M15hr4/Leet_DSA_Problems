class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:


        n = len(nums)
        target = sorted(nums)

        # KMP prefix function for a pattern
        def prefix_function(pattern):
            m = len(pattern)
            pi = [0] * m

            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = pi[j - 1]

                if pattern[i] == pattern[j]:
                    j += 1

                pi[i] = j

            return pi

        # Check whether pattern is a cyclic rotation of block
        def is_rotation(block, pattern):
            k = len(block)
            pi = prefix_function(pattern)

            j = 0

            # Search pattern in block + block.
            # Only need the first 2*k - 1 elements.
            for i in range(2 * k - 1):
                x = block[i % k]

                while j > 0 and x != pattern[j]:
                    j = pi[j - 1]

                if x == pattern[j]:
                    j += 1

                if j == k:
                    return True

            return False

        ans = 0

        # Enumerate divisors of n
        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                block = nums[start:start + k]
                pattern = target[start:start + k]

                if not is_rotation(block, pattern):
                    valid = False
                    break

            if valid:
                ans += k

        return ans
        