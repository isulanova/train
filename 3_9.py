n = int(input())
data = {}
for i in range(n):
    k = int(input())
    while k >= 1:
        lang = input()
        if lang not in data:
            data[lang] = 1
        else:
            data[lang] += 1
        k -= 1
all_know = []
one_know = []
for person in data:
    if data[person] == n:
        all_know.append(person)
    if data[person] >= 1:
        one_know.append(person)
all_know = list(set(all_know))
print(len(all_know))
print(*all_know, sep="\n")
one_know = list(set(one_know))
print(len(one_know))
print(*one_know, sep="\n")