import sys

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()

s_len = len(s)
p_len = len(p)

flag = False
for i in range(s_len):
    if s[i] == p[0] and (i + p_len <= s_len):
        if s[i : i + len(p)] == p:
            flag = True
            break
if flag:
    print(1)
else:
    print(0)
