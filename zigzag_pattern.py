class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array of empty strings for all rows
        rows = [''] * numRows
        current_row = 0
        direction = -1

        for char in s:
            rows[current_row] += char
            # If we reach the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1
            current_row += direction

        # Combine all rows into one string
        return ''.join(rows)

sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
output = sol.convert(s, numRows)
print(output)  

s = "PAYPALISHIRING"
numRows = 4
output = sol.convert(s, numRows)
print(output)  

s = "A"
numRows = 1
output = sol.convert(s, numRows)
print(output)  
