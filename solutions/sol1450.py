import sys
from itertools import combinations
from bisect import bisect_right

input = sys.stdin.read


# 1450 냅색문제
# 무게제한이 있는 가방에 물건을 담을 수 있는 경우의 수를 구하는 문제
# 주어진 물건들의 무게의 부분집합 중 합이 무게제한보다 작거나 같은 것의 갯수를 구해야한다
# 단순히 풀면 물건 N개가 각각 포함되는가 포함되지 않는가 두가지 경우가 있기 때문에 O(2^N)의 시간복잡도를 보인다
# meet in the middle 알고리즘을 사용하면 이를 획기적으로 줄일 수 있다.
def sol1450():
    n, c, *items = map(int, input().split())

    # 주어진 물건들의 무게 리스트를 절반으로 분할
    left, right = items[:n // 2], items[n // 2:]

    # left 에 속한 물건들을 조합하여 얻을 수 있는 합(key)과 그 합을 얻을 수 있는 경우의 수(value)를 구한다
    # 단순히 리스트에 넣는 방법도 있지만 중복되는 값이 많은 경우 시간을 줄일 수 있다.
    ls = {}
    for case in [map(sum, combinations(left, i)) for i in range(len(left) + 1)]:
        for s in case:
            ls[s] = ls.get(s, 0) + 1

    # right 에 속한 물건들을 조합하여 얻을 수 있는 합들을 모두 구한다.(중복제거 X)
    rs = []
    for case in [map(sum, combinations(right, i)) for i in range(len(right) + 1)]:
        for s in case:
            rs.append(s)

    answer = 0
    # right 의 합은 이분탐색을 위해 정렬
    rs.sort()

    # left 의 합들에 대해 right 의 합과 더해 c를 넘지않는 경우의 수를 센다
    for s, cnt in ls.items():
        # left 의 합만으로 c를 넘는다면 패스
        if s > c:
            continue

        # right 의 합중 c - s 를 넘지 않는것의 갯수를 이진탐색으로 구한다
        answer += bisect_right(rs, c - s) * cnt

    return answer
