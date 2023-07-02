n = int(input())
tshirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))
i_pants = 0
diffs = []
diff = tshirts[0] + pants[0]
res = [0, 0]
for i_tsirts in range(len(tshirts)):
    while i_pants < len(pants) and pants[i_pants] < tshirts[i_tsirts]:
        diffs.append(tshirts[i_tsirts] - pants[i_pants])
        if tshirts[i_tsirts] - pants[i_pants] < diff:
            diff = tshirts[i_tsirts] - pants[i_pants]
            res[0] = tshirts[i_tsirts]
            res[1] = pants[i_pants]
        i_pants += 1
    if i_pants < len(pants):
        diffs.append(pants[i_pants] - tshirts[i_tsirts])
        if pants[i_pants] - tshirts[i_tsirts] < diff:
            diff = pants[i_pants] - tshirts[i_tsirts]
            res[0] = tshirts[i_tsirts]
            res[1] = pants[i_pants]
print(res[0], res[1])