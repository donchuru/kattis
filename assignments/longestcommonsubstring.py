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

# check if the substring is a valid substring of ALL the strings
def valid_substring(substr, strings):
    for i in range(len(strings)):
        if substr not in strings[i]:
            return False
        
    return True

def lcs(strings):
    # count how much of a substring from the first str is shared among the rest
    sublen = 0
    firstlen = len(strings[0])

    for i in range(firstlen):
        for j in range(firstlen - i + 1):
            if (valid_substring(strings[0][i:i+j], strings)):
                if (j > sublen):
                    sublen += 1
    return sublen

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

print((lcs(strings)))
