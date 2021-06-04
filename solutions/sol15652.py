import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


# 15652 N과 M (4)
# 1부터 N 까지의 수로 이루어진 수열에서
# 중복을 허용하여 M개를 고른 부분 수열중 오름차순인 것을 모두 구하는 문제

# 직접 완전탐색을 구현한 풀이
def sol15652():
    n, m = map(int, input().split())
    answer = []
    dfs(n, m, 1, [], answer)
    print('\n'.join(map(' '.join, answer)))


def dfs(n, m, idx, seq, answer):
    if (len(seq) == m):
        answer.append(seq[:])
        return
    for i in range(idx, n + 1):
        seq.append(str(i))
        dfs(n, m, i, seq, answer)
        seq.pop()


# itertools 모듈의 combinations_with_replacement 클래스를 활용한 풀이
def sol15652_2():
    n, m = map(int, input().split())
    print('\n'.join(map(' '.join, combinations_with_replacement(map(str, range(1, n+1)), m))))
