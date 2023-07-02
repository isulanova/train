n = int(input())
peaks = [0]
right_peak = [0]
left_peak = [0]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    y0 = peaks[i-1]
    y1 = temp[1]
    if y1-y0 <= 0:
        diff = 0
    else:
        diff = y1-y0
    peaks.append(y1)
    right_peak.append(diff)
peaks.append(0)
for i in range(n, 0, -1):
    y0 = peaks[i+1]
    y1 = peaks[i]
    if y1-y0 <= 0:
        diff = 0
    else:
        diff = y1-y0
    left_peak.append(diff)
m = int(input())
for i in range(m):
    temp = list(map(int, input().split()))
    if temp[0] < temp[1]:
        print(sum(right_peak[temp[0]+1:temp[1]+1]))
    elif temp[0] > temp[1]:
        print(sum(left_peak[n-temp[0]+2:n-temp[1]+2]))
    else:
        print(peaks[temp[0]])