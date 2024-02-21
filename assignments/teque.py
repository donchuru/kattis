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

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

d1, d2 = deque(), deque()

for i in range(n):
    command_input = sys.stdin.readline
    command = command_input().split()

    if command[0] == "push_back":
        d2.append( int(command[1]) )

        # rebalance our deques
        if len(d2) - len(d1) > 1:
            shift_to_d1 = d2.popleft()
            d1.append(shift_to_d1)

    elif command[0] == "push_front":
        d1.appendleft( int(command[1]) )

        # rebalance our deques
        if len(d1) - len(d2) > 1:
            shift_to_d2 = d1.pop()
            d2.appendleft(shift_to_d2)
            
    elif command[0] == "get":
        index = int(command[1])
        if index < len(d1):
            sys.stdout.write( str(d1[index]) + "\n")
        else:
            sys.stdout.write( str(d2[index - len(d1)]) + "\n" )

    elif command[0] == "push_middle":

        if len(d2) > len(d1):
            shift_to_d1 = d2.popleft()
            d1.append(shift_to_d1)
        d2.appendleft(int(command[1]))

    # print("d1", d1, "d2", d2)
