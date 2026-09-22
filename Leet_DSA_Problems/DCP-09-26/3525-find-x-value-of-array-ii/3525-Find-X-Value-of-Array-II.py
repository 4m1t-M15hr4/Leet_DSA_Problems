
from typing import List


class ST:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.st = [[0] * (k + 1) for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1, nums)

    def merge(self, line1, line2):
        k = self.k
        new_line = line1[:]
        new_line[k] = (line1[k] * line2[k]) % k

        for r in range(k):
            new_line[(r * line1[k]) % k] += line2[r]

        return new_line

    def build(self, node, l, r, nums):
        if l == r:
            rem = nums[l] % self.k
            self.st[node][rem] = 1
            self.st[node][self.k] = rem
            return self.st[node]

        mid = l + (r - l) // 2

        left = self.build(node * 2, l, mid, nums)
        right = self.build(node * 2 + 1, mid + 1, r, nums)

        self.st[node] = self.merge(left, right)
        return self.st[node]

    def update(self, node, l, r, i, val):
        if l == r:
            self.st[node] = [0] * (self.k + 1)
            rem = val % self.k
            self.st[node][rem] = 1
            self.st[node][self.k] = rem
            return self.st[node]

        mid = l + (r - l) // 2

        if i <= mid:
            self.update(node * 2, l, mid, i, val)
        else:
            self.update(node * 2 + 1, mid + 1, r, i, val)

        self.st[node] = self.merge(
            self.st[node * 2],
            self.st[node * 2 + 1]
        )

        return self.st[node]

    def query(self, node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return self.st[node]

        if r < ql or l > qr:
            line = [0] * (self.k + 1)
            line[self.k] = 1 % self.k
            return line

        mid = l + (r - l) // 2

        left = self.query(node * 2, l, mid, ql, qr)
        right = self.query(node * 2 + 1, mid + 1, r, ql, qr)

        return self.merge(left, right)


class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)
        st = ST(nums, k)
        result = []

        for i, val, start, x in queries:
            st.update(1, 0, n - 1, i, val)

            line = st.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            result.append(line[x])

        return result
