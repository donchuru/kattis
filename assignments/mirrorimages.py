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
t = int(input())

for i in range(t):
    rows, cols = map(int, input().split())

    matrix = []

    for r in range(rows):
        matrix.append( list(input()) )

    flipped_matrix = []

    for r in range(rows):
        curr_row = []
        for c in range(cols):
            curr_row.append( matrix[(rows - 1) - r][(cols - 1) - c] )
        flipped_matrix.append(curr_row)

    print('Test', i + 1)
    for r in range(rows):
        print("".join(flipped_matrix[r]))
