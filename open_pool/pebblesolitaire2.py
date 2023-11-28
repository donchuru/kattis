"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

def solitare(game, rem_pegs):
    min_pegs = float('inf')
    def dfs(game, rem_pegs):
        nonlocal min_pegs

        if rem_pegs == 1:
            return 1
        
        # right moves
        for i in range(len(game)):
            if game[i] == 'o':
                if (i + 2 < 23) and game[i+1] == 'o' and game[i+2] == '-':
                    game[i+1] = '-'
                    game[i+2] = 'o'
                    game[i] = '-'
                    min_pegs = min(min_pegs, dfs(game, rem_pegs - 1))
                    game[i+1] = 'o'
                    game[i+2] = '-'
                    game[i] = 'o'

        # left moves
        for i in range(len(game)-1, -1, -1):
            if game[i] == 'o':
                if (i-2 >= 0) and game[i-1] == 'o' and game[i-2] == '-':
                    game[i-1] = '-'
                    game[i-2] = 'o'
                    game[i] = '-'
                    min_pegs = min(min_pegs, dfs(game, rem_pegs - 1))
                    game[i-1] = 'o'
                    game[i-2] = '-'
                    game[i] = 'o'

        min_pegs = min(rem_pegs, min_pegs)        
        return min_pegs
    
    return dfs(game, rem_pegs)

n = int(input())
for i in range(n):
    game = list(input())
    init_pegs = game.count('o')
    
    print(solitare(game, init_pegs))
    
