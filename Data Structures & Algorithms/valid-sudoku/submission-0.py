class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            for col in range(9):

                value = board[row][col]

                if value == '.':
                    continue

                for checkCol in range(9):
                    if checkCol != col and board[row][checkCol] == value:
                        return False

                for checkRow in range(9):
                    if checkRow != row and board[checkRow][col] == value:
                        return False

                boxRowStart = (row // 3) * 3
                boxColStart = (col // 3) * 3

                for checkRow in range(boxRowStart, (boxRowStart + 3)):
                    for checkCol in range(boxColStart, (boxColStart + 3)):
                        if (checkRow != row or checkCol != col) and (board[checkRow][checkCol] == value):
                            return False

        return True