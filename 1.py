import os

if (os.stat("input.txt").st_size != 0) and (os.path.exists("input.txt")):
    file = open("input.txt", "r")
    dict = {}
    for str in file:
        for letter in str:
            if letter != '\n' and letter != ' ':
                if letter not in dict:
                    dict[letter] = 0
                dict[letter] += 1
    if len(dict) != 0:
        maximum = max(dict.values())
        dict = sorted(dict.items())
        for i in reversed(range(maximum)):
            for letter in dict:
                if letter[1] > i:
                    print("#", end='')
                else:
                    print(" ", end='')
            print()
        for letter in dict:
            print(letter[0], end='')
else:
    print()