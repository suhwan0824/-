import sys

t = int(sys.stdin.readline().rstrip())

result = []
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    dial = []
    for i in range(n):
        dial.append(sys.stdin.readline().rstrip())
    dial.sort()

    flag = True
    for i in range(n - 1):
        dial_len = len(dial[i])
        if dial[i] == dial[i + 1][:dial_len]:
            flag = False
            break
    result.append(flag)

for ele in result:
    if ele:
        print("YES")
    else:
        print("NO")
