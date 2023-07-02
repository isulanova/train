a, b, c, d, e, f = [float(input()) for _ in range(6)]
if a==b==e:
    a = a/a
    b = b/b
    e = e/e
if c==d==f:
    c = c/c
    d = d/d
    f = f/f
if a==c!=0 and b==d!=0 and e==f!=0:
    print(1, format(-c / d, ".5f"), format(f / d, ".5f"))
elif a==b==c==d==e==f==0:
    print(5)
elif a==b==e==0 and c!= 0 and d!=0 and f!=0:
    print(1, format(-c / d, ".5f"), format(f / d, ".5f"))
elif a!=0 and b!=0 and e!=0 and c==d==f==0:
    print(1, format(-a/b, ".5f"), format(e/b, ".5f"))
elif (a==b==0 and e != 0) or (c==d==0 and f!=0):
    print(0)
elif a!=0:
    if (a*d-c*b)!=0:
        y=(f*a-c*e)/(a*d-c*b)
        x=(e-b*y)/a
        print(2, format(x, ".5f"), format(y, ".5f"))
    elif (a*d-c*b)==0:
        if (f*a-c*e)==0:
            print(5)
        if (f * a - c * e) != 0:
            print(0)
elif a==0:
    if b!= 0 and c!=0:
        y=e/b
        x = f/c - (d*e)/(c*b)
        print(2, format(x, ".5f"), format(y, ".5f"))
    if b != 0 and c == 0 and e!=0:
        y = e/b
        print(4, format(y, ".5f"))
elif b!=0:
    if (b*c-a*d)!=0:
        x=(f*b-d*e)/(b*c-a*d)
        y=(e-a*x)/b
        print(2, format(x, ".5f"), format(y, ".5f"))
    elif (b*c-a*d)==0:
        if (f*b-d*e)==0:
            print(5)
        if (f * b - d * e) != 0:
            print(0)
elif b==0:
    if a!=0 and d!=0:
        x=e/a
        y = f/d - (c*e)/(a*b)
        print(2, format(x, ".5f"), format(y, ".5f"))
    if a != 0 and d == 0 and e!=0:
        x = e/a
        print(3, format(x, ".5f"))
elif c!=0:
    if (b*c-a*d)!=0:
        y=(e*c-a*f)/(b*c-a*d)
        x=(f-d*y)/c
        print(2, format(x, ".5f"), format(y, ".5f"))
    elif (b*c-a*d)==0:
        if (e*c-a*f) ==0:
            print(5)
        if (e*c-a*f) != 0:
            print(0)
elif c==0:
    if a!=0 and d!=0: #c==0
        y=f/d
        x = e/a - (b*f)/(a*d)
        print(2, format(x, ".5f"), format(y, ".5f"))
    if a != 0 and d == 0 and f!=0:
        y = f/d
        print(4, format(y, ".5f"))
elif (d!=0):
    if (a*d-b*c)!=0:
        x=(e*d-b*f)/(a*d-b*c)
        y=(f-c*x)/d
        print(2, format(x, ".5f"), format(y, ".5f"))
    elif (a*d-b*c)==0:
        if (e*d-b*f) ==0:
            print(5)
        if (e*d-b*f) != 0:
            print(0)
elif d==0:
    if b!=0 and c!=0: #d==0
        x=f/c
        y = e/b - (a*f)/(c*b)
        print(2, format(x, ".5f"), format(y, ".5f"))
    if b != 0 and c == 0 and f!=0:
        x = f/c
        print(3, format(x, ".5f"))
elif a==c==0:
    if (e/b == f/d):
        print(4, format(e/b, ".5f"))
    else:
        print(0)
elif b==d==0:
    if (e/c == f/c):
        print(3, format(e/a, ".5f"))
    else:
        print(0)
