import sys
def preprocess(pattern):
    p_len = len(pattern)
    arr = [0] * p_len

    j = 0
    for i in range(1, p_len):
        while j > 0 and pattern[i] != pattern[j]:
            j = arr[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            arr[i] = j
    return arr

def kmp(string, pattern):
    arr = preprocess(pattern)
    n = len(string)
    m = len(pattern)

    j = 0
    for i in range(n):
        while j > 0 and string[i] != pattern[j]:
            j = arr[j - 1]

        if string[i] == pattern[j]:
            if j == n - 1:
                return 1
            else:
                j += 1
    return 0

string = sys.stdin.readline().rstrip()
pattern = sys.stdin.readline().rstrip()
print(kmp(string, pattern))
