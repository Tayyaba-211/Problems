class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for c in s:
            rows[current_row] += c
            # Change direction if at the first or last row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move to the next row
            current_row += 1 if going_down else -1

        # Combine all rows into one final string
        return ''.join(rows)
