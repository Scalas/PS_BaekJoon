import sys
from bisect import bisect_left

input = sys.stdin.readline


# 1059 좋은 구간
# 수의 집합 S와 그중 최댓값을 넘지않는 양의정수 n이 주어졌을 때
# 1. A < B
# 2. A <= x <= B 를 만족하는 모든 x가 집합 S에 속하지 않음
# 3. A <= n <= B
# 위 세 가지 조건을 만족하는 양의 정수 A, B의 쌍의 갯수를 구하는 문제
def sol1059():
    input()
    # 수열의 수를 정렬
    # 구간의 최솟값 경계로 사용하기 위해 0을 삽입
    seq = [0, *map(int, input().split())]
    seq.sort()

    # 구간이 포함해야할 수
    n = int(input())

    # 이분탐색으로 수열에서 n을 탐색
    ni = bisect_left(seq, n)

    # 포함해야할 수가 집합에 포함될 경우
    if seq[ni] == n:
        return 0

    # 구간 내에서 n 이하의 수 하나, n 이상의 수 하나를 골라
    # 좋은 구간을 만들 수 있음. 단, n이 두 번 골라지는 하나의 경우의 수를 빼야함
    return (n-seq[ni-1]) * (seq[ni]-n) - 1

