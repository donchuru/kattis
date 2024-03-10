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
n = float(input())

# map of all possible angles and the time corresponding to them
angle_to_times = dict()

min_angle, hour_angle = 0, 0

for h in range(12):
    for m in range(60):

        a = min_angle - hour_angle

        if a < 0:
            a += 3600

        angle_to_times[a] = (h, m)

        min_angle = (min_angle + 60) % 3600
        hour_angle = (hour_angle + 5) % 3600

time = angle_to_times[n]

if time[0] > 9:
    h_str = str(time[0])
else:
    h_str = '0' + str(time[0])

if time[1] > 9:
    m_str = str(time[1])
else:
    m_str = '0' + str(time[1])

print(h_str+':'+m_str)
