import sys

input = sys.stdin.readline


# 15732 도토리 숨기기
# k개의 규칙에 따라 도토리 d개를 n개의 상자에 나눠담으려 할 때
# 마지막 도토리가 위치한 상자를 구하는 문제(단, 도토리는 왼쪽에서부터 차례대로 담는다)
# 규칙은 u v w 의 형태로 주어지고 u번 상자부터 v번 상자까지 w간격으로 담는다는 의미
def sol15732():
    n, k, d = map(int, input().split())
    rule = [list(map(int, input().split())) for _ in range(k)]

    # 이분탐색으로 담을 수 있는 도토리 갯수가 d개 이상이 되는 첫 상자를 탐색( O(logN) )
    s, e = 1, n
    while s < e:
        mid = (s + e) // 2
        if check(rule, mid) < d:
            s = mid + 1
        else:
            e = mid
    return e


# box번째 상자까지 총 몇개의 도토리를 담을 수 있는지 확인( O(K) )
def check(rule, box):
    res = 0
    for u, v, w in rule:
        if u > box:
            continue
        res += ((min(v, box) - u) // w + 1)
    return res
