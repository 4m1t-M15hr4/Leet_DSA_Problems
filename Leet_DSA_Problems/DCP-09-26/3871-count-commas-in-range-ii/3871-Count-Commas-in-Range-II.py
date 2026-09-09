class Solution(object):
    def countCommas(self, n):
        total_comma = 0
        thres = 1000
        while thres <= n:
            total_comma +=(n - thres + 1)
            thres *= 1000
        return total_comma