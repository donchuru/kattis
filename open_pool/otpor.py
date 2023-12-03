"""
  BEGIN-HEADER
  
  Name: David Onchuru
  
  Student-ID: 1647809

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
"""

resistors_stack = []
arrange_stack = [] # parallel or series

N = int(input())
resistor_map = dict()
l = list(map(float, input().split()))

for i in range(N):
    resistor_map["R"+str(i+1)] = l[i]

expression = "(" + input() + ")"

def parallel(res):
    total = 0
    for i in res:
        if i > 0:
            total += (1/i)

    if total > 0:
        return 1/total
    return 0

def series(res):
    return sum(res)

temp_res = []
rs_in_brackets = []

for i in range(len(expression)):
    if expression[i] == ')':
        if arrange_stack and rs_in_brackets:
            a = arrange_stack.pop()
            resistor_cnt = rs_in_brackets.pop()

            for _ in range(resistor_cnt):
                    temp_res.append(resistors_stack.pop())

            for _ in range(min(resistor_cnt-2, len(arrange_stack))):
                arrange_stack.pop()

            if a == "parallel":
                resistors_stack.append(parallel(temp_res))
            elif a == "series":
                resistors_stack.append(series(temp_res))

            temp_res = []
            
            if rs_in_brackets:
                rs_in_brackets[-1] += 1
        

    elif expression[i] == '(':
        rs_in_brackets.append(0)

    elif expression[i] == 'R':
         continue

    elif expression[i] == '-':
        arrange_stack.append("series")
    

    elif expression[i] == "|":
        arrange_stack.append("parallel")


    else:
        r = expression[i-1:i+1]
        resistors_stack.append(resistor_map[r])
        rs_in_brackets[-1] += 1

if resistors_stack:
    print(resistors_stack[-1])
else:
    print(0)
    
