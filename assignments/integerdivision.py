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

n, d = map(int, input().split())
integers = list(map(int, input().split()))

integers.sort()

ptr1, ptr2 = 0, 0
csf = 0
curr = integers[ptr1] // d

while ptr2 < len(integers):
    if (integers[ptr2] // d) != curr:
        dist_btwn = ptr2 - ptr1
        csf += dist_btwn * ((dist_btwn - 1)/2)
        curr = integers[ptr2] // d
        ptr1 = ptr2

    ptr2 += 1

db_final = ptr2 - ptr1
csf += db_final * ((db_final - 1)/2)

print(int(csf))
