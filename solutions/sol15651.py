import sys
from itertools import product


# 15651 N과 M (3)
# 1부터 N 까지의 수로 이루어진 수열에서
# 중복을 허용하여 M개를 고른 부분 수열을 모두 구하는 문제

# 직접 완전탐색을 구현한 풀이
def sol15651():
    n, m = map(int, sys.stdin.readline().split())
    dfs(n, m, [])


def dfs(n, m, seq):
    if (len(seq) == m):
        sys.stdout.write(' '.join(seq) + '\n')
        return

    for num in range(1, n + 1):
        seq.append(str(num))
        dfs(n, m, seq)
        seq.pop()


# itertools 모듈의 product 클래스를 활용한 풀이
# 두 개 이상의 리스트간의 모든 조합을 구하는 product 클래스로 [1, 2, ... , n] 수열 m 개의 모든 조합을 구한다
def sol15651_2():
    n, m = map(int, sys.stdin.readline().split())
    print('\n'.join(map(' '.join, product(map(str, range(1, n + 1)), repeat=m))))
