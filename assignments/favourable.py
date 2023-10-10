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

def count_fav_endings(memo_fav, options_from_pg, start):
    
    def find_f(i):
        if i in memo_fav:
            return memo_fav[i]
        
        options = options_from_pg[i]
        f_possible = find_f(options[0]) + find_f(options[1]) + find_f(options[2])
        memo_fav[i] = f_possible
        return f_possible
    

    return find_f(start)


for i in range(t):
    s = int(input())

    memo_fav = dict()
    options_from_pg = dict()

    for j in range(s):
        line = input().split()

        if len(line) == 4:
            line_tmp = list(map(int, line))
            options_from_pg[line_tmp[0]] = line_tmp[1:]
        
        else:
            if line[1] == "favourably":
                memo_fav[int(line[0])] = 1
            else:
                memo_fav[int(line[0])] = 0

    print(count_fav_endings(memo_fav, options_from_pg, 1))
