board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

def solveSudoku(self, board: List[List[str]]) -> None:
  empty_places = [(row,col) for row in range(9) for col in range(9) if board[row][col] == "."]

  # standard DFS  
  def solve(idx):
      # if there is no empty space in board
      if idx == len(empty_places):
          return True

      row,col = empty_places[idx]
      for n in range(1,10):
          # check for every possible valid value
          if isValid(row,col,str(n)):
              board[row][col] = str(n)

              # after placing that value check further it can be solvable?
              if solve(idx+1):
                  return True
              board[row][col] = "."

      # return False if not solvable
      return False

  # check if given number can take place that empty place                        
  def isValid(row,col,n):
      topLeftRow = row - row%3  # 3*(row//3)
      topLeftCol = col - col%3  # 3*(col//3)

      for i in range(9):
          # check in that row and col
          if board[row][i] == n or board[i][col] == n:
              return False

          # check in that sub-board (l -> r, t -> b)
          if board[ topLeftRow + i%3 ][ topLeftCol + i//3 ] == n:
              return False
      return True

  solve(0)
  
solveSudoku(board)
