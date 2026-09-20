class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right =m * n - 1
        while left <= right:
            mid = (left + right )// 2
            row = mid // n
            cow = mid % n
            if matrix[row][cow] == target:
                return True
            elif matrix[row][cow] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


        # arr = []
        # for i in range(n):
        #     for j in range(n):
        #         arr.append(matrix[i][j])
        # if target not in arr:
        #     return False
        # return True
            