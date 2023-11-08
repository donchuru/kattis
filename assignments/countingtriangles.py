# """
#   BEGIN-HEADER
  
#   Name: David Onchuru
  
#   Student-ID: 1647809

#   List any resources you used below (eg. urls, name of the algorithm from our code archive).
#   Remember, you are permitted to get help with general concepts about algorithms
#   and problem solving, but you are not permitted to hunt down solutions to
#   these particular problems!

#   List any classmate you discussed the problem with. Remember, you can only
#   have high-level verbal discussions. No code should be shared, developed,
#   or even looked at in these chats. No formulas or pseudocode should be
#   written or shared in these chats.

#   <List Classmates Here>

#   By submitting this code, you are agreeing that you have solved in accordance
#   with the collaboration policy in CMPUT 303/403.

#   END-HEADER
# """

from sys import stdin

def intersecting(i, j):
    l1 = line_segments[i]
    l2 = line_segments[j]

    a1, b1 = (l1[3] - l1[1]), (l1[0] - l1[2])
    c1 = a1 * (l1[0]) + b1 * (l1[1])

    a2, b2 = (l2[3] - l2[1]), (l2[0] - l2[2])
    c2 = a2 * (l2[0]) + b2 * (l2[1])

    det = (a1 * b2) - (a2 * b1)

    # if lines are parallel
    if det == 0:
        return None

    #intersection point
    x, y  = (b2 * c1 - b1 * c2) / det, (a1 * c2 - a2 * c1) / det

    # check if intersection point lies within the bounds of the line segments
    if ( min(l1[0], l1[2]) <= x <= max(l1[0], l1[2]) ) and ( min(l1[1], l1[3]) <= y <= max(l1[1], l1[3]) ) and ( min(l2[0], l2[2]) <= x <= max(l2[0], l2[2]) ) and ( min(l2[1], l2[3]) <= y <= max(l2[1], l2[3]) ):
        return [x, y]
    
def is_triangle(i, j, k):
    l2l3 = intersections[j, k]
    l1l2 = intersections[i, j]
    l1l3 = intersections[i, k]

    # if lines are parallel
    if not l1l2 or not l2l3 or not l1l3:
        return False
    # no 2 intersection points are the same
    if l1l2 != l2l3 and l1l2 != l1l3 and l2l3 != l1l3:
        return True

intersections = {}

def compute_all_intersections():
    n = len(line_segments)
    for i in range(n):
        for j in range(i + 1, n):
                intersections[i,j] = intersections[j,i] = (intersecting(i,j))

def count_triangles():
    n = len(line_segments)
    count = 0
    compute_all_intersections()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_triangle(i, j, k):
                    count += 1

    return count

line_segments = []
for ip in stdin:
    if ip.strip() == "0":
        break

    n = int(ip)
    for i in range(n):
        points = list(map(float, input().split()))
        line_segments.append(points)

    print(count_triangles())
    line_segments.clear()
    intersections.clear()
