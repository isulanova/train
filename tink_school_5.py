n = int(input())
if n == 1:
    print(len(input()))
else:
    tabuns = []
    dict = {"a": 0, "b": 0, "c": 0}
    for i in range(n):
        str = input()
        temp = dict.copy()
        for s in str:
            if s == "a":
                temp["a"] += 1
            elif s == "b":
                temp["b"] += 1
            elif s == "c":
                temp["c"] += 1
        tabuns.append(temp)

    res = {}

    for i in range(len(tabuns)):
        a = []
        b = []
        c = []
        a.append(tabuns[i]["a"])
        b.append(tabuns[i]["b"])
        c.append(tabuns[i]["c"])
        for j in range(len(tabuns)):
            if i != j:
                a.append(tabuns[j]["a"])
                b.append(tabuns[j]["b"])
                c.append(tabuns[j]["c"])
                ugliness = max(sum(a), sum(b), sum(c)) - min(sum(a), sum(b), sum(c))
                power = sum(a) + sum(b) + sum(c)
                if ugliness not in res:
                    res[ugliness] = power
                else:
                    if res[ugliness] < power:
                        res[ugliness] = power


    min_ugliness = ugliness
    max_power = power

    print(res[min(res.keys())])
