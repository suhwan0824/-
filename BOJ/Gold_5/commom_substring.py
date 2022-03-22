import sys

s1, s2 = input().rstrip(), input().rstrip()

w = len(s1)
h = len(s2)

dp = [[0] * (h + 1) for _ in range(w + 1)]

for i in range(1, w + 1):
    for j in range(1, h + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

res = 0
for ele in dp:
    tmp = max(ele)
    res = max(res, tmp)
print(res)

