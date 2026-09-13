class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            num_set = set()
            for num in row:
                if(num != '.'):
                    if num in num_set:
                        return False
                    else:
                        num_set.add(num)

        for j in range(len(board)):
            num_set = set()
            for i in range(len(board)):
                if(board[i][j] != '.'):
                    if board[i][j] in num_set:
                        return False
                    else:
                        num_set.add(board[i][j])

        for i in [1,4,7]:
            for j in [1,4,7]:
                num_set = set()
                num = board[i][j]
                if(num != '.'):
                    num_set.add(num)

                if board[i-1][j-1] in num_set and board[i-1][j-1] != '.': 
                    return False 
                elif board[i-1][j-1] != '.': 
                    num_set.add(board[i-1][j-1])

                if board[i-1][j] in num_set and board[i-1][j] != '.': 
                    return False 
                elif board[i-1][j] != '.': 
                    num_set.add(board[i-1][j])

                if board[i-1][j+1] in num_set and board[i-1][j+1] != '.': 
                    return False 
                elif board[i-1][j+1] != '.': 
                    num_set.add(board[i-1][j+1])

                if board[i][j-1] in num_set and board[i][j-1] != '.': 
                    return False 
                elif board[i][j-1] != '.': 
                    num_set.add(board[i][j-1])

                if board[i][j+1] in num_set and board[i][j+1] != '.': 
                    return False 
                elif board[i][j+1] != '.': 
                    num_set.add(board[i][j+1])

                if board[i+1][j-1] in num_set and board[i+1][j-1] != '.': 
                    return False 
                elif board[i+1][j-1] != '.': 
                    num_set.add(board[i+1][j-1])

                if board[i+1][j] in num_set and board[i+1][j] != '.': 
                    return False 
                elif board[i+1][j] != '.':
                    num_set.add(board[i+1][j])

                if board[i+1][j+1] in num_set and board[i+1][j+1] != '.': 
                    return False 
                elif board[i+1][j+1] != '.': 
                    num_set.add(board[i+1][j+1])


        return True