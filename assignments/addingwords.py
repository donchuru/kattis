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

hm = dict()
symbols = ["+", "-", "="]

def operate(calc_op):
    for i in calc_op:
        if i not in symbols and i not in hm:
            print(" ".join(calc_op) + " unknown")
            return
    
    total = hm[calc_op[0]]
    for i in range(2, len(calc_op)):
        if calc_op[i-1] == "+":
            total += hm[calc_op[i]]
        elif calc_op[i-1] == "-":
            total -= hm[calc_op[i]]

    if total not in hm.values():
        print(" ".join(calc_op) + " unknown")
    else:
        print( " ".join(calc_op) + " " + list(hm.keys())[list(hm.values()).index(total)])

            
for line in stdin:
    line_list = line.split()
    
    if line_list[0] == "def":
        hm[line_list[1]] = int(line_list[2])
        # print("hm", hm)

    elif line_list[0] == "calc":
        calc_op = line_list[1:]
        operate(calc_op)

    elif line_list[0] == "clear":
        hm.clear()
