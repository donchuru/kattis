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

from collections import defaultdict

n = int(input())
s = list(map(str, input().split()))
m = int(input())

translations = defaultdict(list)
d_to_corr_incorr = defaultdict(list) # 2 elements -> no. of corrects and no. of incorrects
multi = False

for i in range(m):
    d, e, c = map(str, input().split())

    if d not in d_to_corr_incorr:
        d_to_corr_incorr[d] = [0, 0]

    if c == "correct":
        d_to_corr_incorr[d][0] += 1
    else:
        d_to_corr_incorr[d][1] += 1

    translations[d].append((e, c))

if (d_to_corr_incorr[d][0] + d_to_corr_incorr[d][1]) > 1:
    multi = True

# print(translations)
# print(d_to_corr_incorr)

if multi:
    # count number of total ways to translate for each position in s
    # m * n * ... 
    total, corrects, incorrects = 1, 1, 1
    for i in s:
        total *= (d_to_corr_incorr[i][0] + d_to_corr_incorr[i][1])
        corrects *= d_to_corr_incorr[i][0]
        incorrects *= d_to_corr_incorr[i][1]

    if corrects >= incorrects:
        print(corrects, "correct")
        print(total - corrects, "incorrect")
    else:
        print(total - incorrects, "correct")
        print(incorrects, "incorrect")

else:
    # translate s
    s_english = []
    incorrect = False
    for i in s:
        s_english.append(translations[i][0][0])
        # if translations[i][0][1] == "incorrect":
        # print("d_to_corr_incorr[i][0][1]", d_to_corr_incorr[i][0][1])
        if d_to_corr_incorr[i][1] == 1:
            incorrect = True

    print(*s_english)
    if incorrect:
        print("incorrect")
    else:
        print("correct")
