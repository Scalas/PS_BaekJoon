import sys
from itertools import combinations


# 15650 N과 M (2)
# 1부터 N까지의 수로 이루어진 수열에서
# M개를 고른 부분 수열을 모두 구하는 문제 (조합)


# 직접 완전탐색을 구현한 풀이
def sol15650():
    n, m = map(int, sys.stdin.readline().split())
    dfs(n, m, [], 0)


def dfs(n, m, seq, idx):
    if (len(seq) == m):
        sys.stdout.write(' '.join(seq) + '\n')

    for num in range(idx + 1, n + 1):
        seq.append(str(num))
        dfs(n, m, seq, num)
        seq.pop()


# itertools 모듈의 combinations 클래스를 활용한 풀이
def sol15650_2():
    n, m = map(int, sys.stdin.readline().split())
    print('\n'.join(map(' '.join, combinations(map(str, range(1, n + 1)), m))))
