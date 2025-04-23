# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]


class Solution:
    def generate(self, numRows: int):
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)  # Create a row with all 1s
            for j in range(1, i):  # Compute inner elements
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)  # Add row to triangle
        
        return triangle
    
print(Solution().generate(5))