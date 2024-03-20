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

def cuberoot(x):
    low = 0
    high = x
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if mid ** 3 > x:
            high = mid - 1
        elif mid ** 3 < x:
            low = mid + 1
        else:
            return int(mid)

    res_dict = dict()
    res_dict[abs(x - (low ** 3))] = low
    res_dict[abs(x - (mid ** 3))] = mid
    res_dict[abs(x - (high ** 3))] = high

    res = res_dict[min(res_dict.keys())]

    return res
                
for line in stdin:
    x = int(line)
    print(cuberoot(x))
