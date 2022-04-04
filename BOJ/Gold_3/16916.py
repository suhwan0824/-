import sys

def get_pi(pat):
    n = len(pat)
    pi = [0] * n

    idx = 0
    for i in range(1, n):
        while idx > 0 and pat[i] != pat[idx]:
            idx = pi[idx - 1]

        if pat[i] == pat[idx]:
            idx += 1
            pi[i] = idx
    return pi

def kmp(txt, pat):
    n = len(txt)
    m = len(pat)
    pi = get_pi(pat)

    result = []
    idx = 0
    for i in range(n):
        while idx > 0 and txt[i] != pat[idx]:
            idx = pi[idx - 1]

        if txt[i] == pat[idx]:
            if idx == m - 1:
                return 1
            else:
                idx += 1
    return 0

s = sys.stdin.readline().rstrip()
p = sys.stdin.readline().rstrip()
print(kmp(s, p))
