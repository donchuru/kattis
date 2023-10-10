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

n, m = map(int, input().split())

inputs = []
for i in range(n):
    inputs.append(list(map(int, input().split())))

# print(inputs)


# map of timestamps when each swather finished each stage (in order) 
# timestamps start at 1
finished_ts = [[0 for col in range(m)] for row in range(n)]

# finish swather 0
finished_ts[0][0] = inputs[0][0]
for c in range(1, m):
    finished_ts[0][c] += finished_ts[0][c-1] + inputs[0][c]

# finish stage 0
for r in range(1, n):
    finished_ts[r][0] += ( inputs[r][0] + finished_ts[r-1][0] )

for c in range(1, m):
    for r in range(1, n):
        finished_ts[r][c] += ( (max(finished_ts[r-1][c], finished_ts[r][c-1])) + (inputs[r][c]) )


output = []
for r in finished_ts:
    output.append(r[-1])

print(*output)
