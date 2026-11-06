class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: x[1])
        queries = [(i, q) for i, q in enumerate(queries)]
        queries.sort(key=lambda x: x[1])

        res = [0] * len(queries)
        using = defaultdict(int)

        l, r = 0, 0

        for idx, q in queries:
            while r < len(logs) and logs[r][1] <= q:
                s = logs[r][0]
                using[s] += 1
                r += 1

            while l < r and logs[l][1] < q - x:
                s = logs[l][0]
                using[s] -= 1
                if using[s] == 0:
                    del using[s]
                l += 1

            res[idx] = n - len(using)

        return res