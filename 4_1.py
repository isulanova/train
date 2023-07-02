n = int(input())
dict = {}
for i in range(n):
    temp = list(map(str, input().split()))
    dict[temp[0]] = temp[1]
find = input()
for word in dict:
    if word == find:
        print(dict[word])
    elif dict[word] == find:
        print(word)