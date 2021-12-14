import sys
from collections import Counter

input = sys.stdin.read


# 1371 가장 많은 글자
# 주어진 문자열에서 가장 많이 등장한 문자를 구하는 문제
# 최대 빈도수를 가지는 문자가 여러개일 경우 알파벳순으로 공백없이 출력
def sol1371():
    count = Counter(''.join(input().split()))
    sres = sorted(count.keys(), key = lambda x: (count[x], x))
    max_val = max(count.values())
    return ''.join([c for c in sres if count[c] == max_val])
