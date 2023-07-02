nums = list(map(int, input().split()))
g = input()
s = input()
g_dict = {}
count = 0
for letter in g:
    if letter not in g_dict:
        g_dict[letter] = 1
    else:
        g_dict[letter] += 1
temp = {}
for j in range(len(g)):
    if s[j] not in temp:
        temp[s[j]] = 1
    else:
        temp[s[j]] += 1
j = 0
for i in range(len(g), len(s)):
    if temp == g_dict:
        count += 1
    if temp[s[j]] == 1:
        temp.pop(s[j])
    else:
        temp[s[j]] -= 1
    j += 1
    if s[i] not in temp:
        temp[s[i]] = 1
    else:
        temp[s[i]] += 1
    if i == len(s) - 1:
        if temp == g_dict:
            count += 1
print(count)

