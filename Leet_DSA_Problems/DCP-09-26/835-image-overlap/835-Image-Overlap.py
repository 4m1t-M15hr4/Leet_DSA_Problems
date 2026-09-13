class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ans = 0

        for row_s in range(-(n -1), n):
            for col_s in range(-(n- 1), n):

                overlap  = 0
                for r in range(n):
                    for c in range(n):
                        r2 = r + row_s
                        c2 = c + col_s

                        if 0 <= r2 < n and 0 <= c2 < n:
                            if img1[r][c] == 1 and img2[r2][c2] == 1:
                                overlap += 1
                ans = max(ans, overlap)
        return ans

        