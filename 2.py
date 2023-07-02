k = int(input())
str = input()

letters = {}
for i in range(len(str)):
    if str[i] not in letters:
        letters[str[i]] = i
    elif str[i] in letters:
        letters[str[i]].append(i)
print(letters)


