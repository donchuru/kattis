"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  <List Resources Here>

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  <List Classmates Here>

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

from sys import stdin

n = int(input())

def solitare(board) -> tuple:

    ROWS = len(board)
    COLS = len(board[0])

    # visited = dict()
    
    def dfs(board, rem_pegs, moves) -> tuple:
        # b = ""
        # for row in board:
        #     print(b.join(row))
        # print("\n")
        # print("rem_pegs", rem_pegs, moves)

        # if board in visited:
        #     return visited[board]

        nonlocal ROWS, COLS, pegs_left, moves_sf

        # 1 peg -> board solved
        if rem_pegs == 1:
            pegs_left = min(pegs_left, rem_pegs)
            moves_sf = moves
            return (pegs_left, moves_sf)

        for r in range(ROWS):
            for c in range(COLS):

                # Once we see a peg
                if board[r][c] == 'o':
                    # print("we found an o")
                    # Check if any neighbors are also pegs and the neighbor's neighbor is a hole

                    # Up direction
                    if (r - 2 in range(ROWS)) and board[r - 1][c] == 'o' and board[r - 2][c] == '.':
                        board_copy = [list(row) for row in board]
                        board_copy[r][c] = '.'
                        board_copy[r - 1][c] = '.'
                        board_copy[r - 2][c] = 'o'
                        dfs(board_copy, rem_pegs - 1, moves + 1)

                    # Down direction
                    if (r + 2 in range(ROWS)) and board[r + 1][c] == 'o' and board[r + 2][c] == '.':
                        board_copy = [list(row) for row in board]
                        board_copy[r][c] = '.'
                        board_copy[r + 1][c] = '.'
                        board_copy[r + 2][c] = 'o'
                        dfs(board_copy, rem_pegs - 1, moves + 1)

                    # Left direction
                    if (c - 2 in range(COLS)) and board[r][c - 1] == 'o' and board[r][c - 2] == '.':
                        board_copy = [list(row) for row in board]
                        board_copy[r][c] = '.'
                        board_copy[r][c - 1] = '.'
                        board_copy[r][c - 2] = 'o'
                        dfs(board_copy, rem_pegs - 1, moves + 1)

                    # Right direction
                    if (c + 2 in range(COLS)) and board[r][c + 1] == 'o' and board[r][c + 2] == '.':
                        board_copy = [list(row) for row in board]
                        board_copy[r][c] = '.'
                        board_copy[r][c + 1] = '.'
                        board_copy[r][c + 2] = 'o'
                        dfs(board_copy, rem_pegs - 1, moves + 1)

        pegs_left = min(rem_pegs, pegs_left)
        moves_sf = max(moves, moves_sf)
        return (rem_pegs, moves)


    total_pegs = sum(row.count('o') for row in board)
    pegs_left = total_pegs
    moves_sf = 0
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'o':
                p, m = dfs(board, total_pegs, 0)
                # print("m", m)
                pegs_left = min(pegs_left, p)

    return (pegs_left, moves_sf)


for i in range(n):
    board = []

    for line in stdin:
        if line != "\n":
            board.append(list(line.strip()))
        else: #process game logic
            break

    # print(board)

    print(solitare(board)[0], solitare(board)[1])
