import sys
from itertools import permutations


# 15649 N과 M (1)
# 1부터 N까지의 수로 이루어진 수열에서
# M개를 고른 부분 수열을 모두 구하는 문제


# 직접 완전탐색을 구현한 풀이
def sol15649():
    n, m = map(int, sys.stdin.readline().split())
    choosed = [False] * n
    dfs(n, m, choosed, [])


def dfs(n, m, choosed, seq):
    if (len(seq) == m):
        sys.stdout.write(' '.join(seq) + '\n')

    for num in range(1, n + 1):
        if choosed[num - 1]:
            continue
        seq.append(str(num))
        choosed[num - 1] = True
        dfs(n, m, choosed, seq)
        seq.pop()
        choosed[num - 1] = False


# itertools 모듈의 permutations 클래스를 활용한 풀이
def sol15649_2():
    n, m = map(int, sys.stdin.readline().split())
    print('\n'.join(map(' '.join, permutations(map(str, range(1, n + 1)), m))))
