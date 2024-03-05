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
import math

tmp = list(input().split())
m = int(tmp[0])
n = int(tmp[1])
r = float(tmp[2])
a_x, a_y, b_x, b_y = map(int, input().split())

y_distance  = (r/n) * abs(b_y - a_y)

arc_radius = (r/n) * (min(a_y, b_y))
angle = abs(b_x - a_x) * (math.pi / m)
arc_len = (arc_radius * angle)

to_origin_and_back = (r/n) * ( (a_y) + (b_y))

print( min((y_distance + arc_len), to_origin_and_back) )
