n = int(input())
dict = {}
count = 0
for i in range(n):
    s = input()
    if s.lower() not in dict:
        dict[s.lower()] = [s]
    else:
        dict[s.lower()].append(s)
text = list(map(str, input().split()))
for word in text:
    if word.lower() in dict:
        if word not in dict[word.lower()]:
            count += 1
    else:
        upper_count = 0
        for letter in word:
            if letter.isupper():
                upper_count += 1
        if upper_count != 1:
            count += 1
print(count)
