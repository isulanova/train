a = int(input())
b = int(input())
c = int(input())
if c < 0:
    print("NO SOLUTION")
else:
    if a != 0:
        x = (c * c - b)/a
        if (a * x + b) >= 0 and int(x) == x:
            print(int(x))
        else:
            print("NO SOLUTION")
    else:
        if b == c*c:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")
