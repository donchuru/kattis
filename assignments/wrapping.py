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

'''
 I recommend you carefully check your code for rotating the boxes before you solve the rest. If you compute rotated boxes properly, the rest is just copy/paste of the appropriate generic algorithm implementations (cite your source).
'''
import math

def point(x, y):
    return (x, y)

def add(p, q):
    return point(p[0] + q[0], p[1] + q[1])

def subtract(p, q):
    return point(p[0] - q[0], p[1] - q[1])

rotate = lambda p, theta, origin=(0, 0): (
    origin[0] + (p[0] - origin[0]) * math.cos(theta) - (p[1] - origin[1]) * math.sin(theta),
    origin[1] + (p[0] - origin[0]) * math.sin(theta) + (p[1] - origin[1]) * math.cos(theta),
)

def remove_middle(a, b, c):
    cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
    return cross < 0 or cross == 0 and dot <= 0


def convex_hull(points):
    spoints = sorted(points)
    hull = []
    for p in spoints + spoints[::-1]:
        while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull

cross2d = lambda v1, v2: v1[0] * v2[1] - v1[1] * v2[0]

def area(p):
    a = 0
    for i in range(len(p) - 1):
        a += cross2d(p[i], p[i + 1])
    a += cross2d(p[-1], p[0])

    return abs(a) / 2.0



# print(rotate((4.5 - 2.444, 3 - 2.2), 26.5))

N = int(input())
for i in range(N):
    boxes_area = 0
    points = [] # all corners of all the boards in the mould
    n = int(input())

    for i in range(n):
        x, y, w, h, v = list(map(float, input().split()))
        boxes_area += (w * h)

        v = abs(v)

        # print(rotate((x - (w/2),y - h), v))
        hrot = rotate((0, h/2), v)
        wrot = rotate((w/2, 0), v)

        # get all 4 corners of the board and add them to points 
        points.append(add(add((x,y), hrot), wrot))
        points.append(add(subtract((x,y), hrot), wrot))
        points.append(subtract(add((x,y), hrot), wrot))
        points.append(subtract(subtract((x,y), hrot), wrot))

    # get convex hull -> list of coordinates
    ch = convex_hull(points)

    print(ch)
    # get hull area
    ch_area = area(ch)

    print(ch_area)

    # get usage
    print(((boxes_area * 100)/ch_area))
