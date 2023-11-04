"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  PyRival repo

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

# lifted from PyRival
to_vec = lambda p1, p2: (j - i for i, j in zip(p1, p2)) # vector btwn 2 points
cross2d = lambda v1, v2: v1[0] * v2[1] - v1[1] * v2[0]
norm_sq = lambda v: sum(i * i for i in v) # magnitude

n = int(input())

for i in range(n):
    line = list(map(int, input().split()))
    p1 = (line[0], line[1])
    p2 = (line[2], line[3])

    line = tuple(to_vec(p1, p2))
    line_mag = norm_sq(line)

    city_to_pos = dict()
    m = int(input())
    for i in range(m):
        cp = list(input().split())
        city_to_pos[cp[0]] = ( int(cp[1]), int(cp[2]) )

    dist_to_city = defaultdict(list)
    res = []

    for i in city_to_pos:
        pos = city_to_pos[i]
        point_to_p1 = tuple(to_vec(pos, p1))

        # cross product btwn line vector and (line to point) vector
        cross_p = cross2d(line, point_to_p1) 
        dist = abs(cross_p / line_mag)

        dist_to_city[dist].append(i)

    print(*dist_to_city[min(dist_to_city.keys())])
