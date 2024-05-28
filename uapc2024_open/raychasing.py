x1, x2, y1, y2 = map(int, input().split())
xs, ys, xr, yr = map(int, input().split())

if ((xs - xr) == -(ys - yr)) and (yr > ys):
    print("top-left")
elif ((xs - xr) == (ys - yr)) and (yr > ys):
    print("top-right")
elif ((xs - xr) == -(ys - yr)) and (ys > yr):
    print("bottom-right")
elif ((xs - xr) == (ys - yr)) and (ys > yr):
    print("bottom-left")
elif (yr > ys) and ((x1 <= xs) and (xs <= x2)):
    print("top")
elif (ys > yr) and ((x1 <= xs) and (xs <= x2)):
    print("bottom")
elif (xs > xr) and ((y1 <= ys) and (ys <= y2)):
    print("left")
elif (xr > xs) and ((y1 <= ys) and (ys <= y2)):
    print("right")
