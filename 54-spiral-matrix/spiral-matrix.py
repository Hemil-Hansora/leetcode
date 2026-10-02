class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        ans = list()
        while top <= bottom and left <= right:
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1

            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for rev_col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][rev_col])
                bottom -= 1

            if left <= right:
                for rev_row in range(bottom, top - 1, -1):
                    ans.append(matrix[rev_row][left])
                left += 1
        return ans
