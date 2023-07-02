first = input()
first_gen = {}
second = input()
second_gen = {}
for i in range(len(first) - 1):
    if first[i:i+2] not in first_gen:
        first_gen[first[i:i+2]] = 1
    else:
        first_gen[first[i:i + 2]] += 1
for i in range(len(second) - 1):
    if second[i:i+2] not in second_gen:
        second_gen[second[i:i+2]] = 1
    else:
        second_gen[second[i:i + 2]] += 1
common = set.intersection(set(first_gen), set(second_gen))
count = 0
for gen in common:
    count += max(first_gen[gen], second_gen[gen])
    print(first_gen[gen], second_gen[gen])
print(first_gen)
print(second_gen)
print(common)
print(count)