temp = list(map(int, input().split()))
if len(temp) != 2:
    print()
else:
    mode = input()
    if temp[0] > 50 or temp[0] < -50 or temp[1] > 50 or temp[1] < -50:
        print()
    else:
        if mode == "freeze":
            if temp[0] > temp[1]:
                print(temp[1])
            elif temp[0] <= temp[1]:
                print(temp[0])
            else:
                print()
        if mode == "heat":
            if temp[0] < temp[1]:
                print(temp[1])
            elif temp[0] >= temp[1]:
                print(temp[0])
            else:
                print()
        if mode == "fan":
            print(temp[0])
        if mode == "auto":
            print(temp[1])
        else:
            print()

