class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        gird = [['#'] * n for _ in range(m)]

        for j in range(m): gird[j][0] ='.'
        for i in range(n): gird[-1][i] ='.'

        return ["".join(row) for row in gird]
        