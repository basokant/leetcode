class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1

        while left <= right:
            mid = (left + right) // 2
            mrow, mcol = mid // len(matrix[0]), mid % len(matrix[0])

            if target == matrix[mrow][mcol]:
                return True
            if target > matrix[mrow][mcol]:
                left = mid + 1
            else:
                right = mid - 1

        return False
