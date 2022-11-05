import sys
from bisect import bisect_right

input = sys.stdin.readline


# 16566 카드 게임
# 1 ~ n 사이의 서로 다른 카드가 m개 주어지고
# 1 ~ n 사이의 카드가 K개 주어진다(이 카드들은 서로 같을 수도 있다.)
# 주어진 k개의 카드에 대해 순서대로 가지고 있는 카드(m개)에서 그 카드보다 큰 카드중 가장 작은 카드를
# 내놓아야 한다고 할 때, 내놓을 카드를 순서대로 구하는 문제
# 단, 내놓지 못하는 경우는 존재하지 않는다.
def sol16566():
    n, m, k = map(int, input().split())
    blue_cards = sorted(map(int, input().split()))

    # 이분탐색으로 매턴 자신이 내야할 카드를 알아낼 수 있지만
    # 한번 사용한 카드를 탐색에서 제외하기 어렵다
    # 그렇다고 이분탐색 위치에서 선형탐색을 하기엔 시간복잡도가 문제가 된다.
    # 이를 해결하기 위해 이미 사용한 연속된 카드들을 하나의 클러스터로 묶어 한번에 스킵 가능하도록 한다.
    answer = []
    cluster = [None] * m
    for card in map(int, input().split()):
        # 사용한 카드를 고를때 이분탐색 결과에서 이미 사용한 클러스터의 마지막 값이 나올 경우 + 1 을 하여 사용하고
        # 사용하지 않은 카드를 고를 경우 그 카드를 사용한다.
        target = bisect_right(blue_cards, card)
        target = find(cluster, target) + (0 if cluster[target] is None else 1)
        cluster[target] = -1
        answer.append(blue_cards[target])

        # 그 후, 사용한 카드 좌우로 사용한 카드 클러스터의 존재를 확인하고
        # union 을 통해 하나의 클러스터로 만든다. 이때, 클러스터의 값은 가장 오른쪽에 있는(가장 큰) 카드의 번호가 된다.
        if target > 0 and cluster[target - 1] is not None:
            union(cluster, target - 1, target)

        if target < m - 1 and cluster[target + 1] is not None:
            union(cluster, target, target + 1)

    return '\n'.join(map(str, answer))


def union(cluster, c1, c2):
    c1 = find(cluster, c1)
    c2 = find(cluster, c2)
    if c1 != c2:
        cluster[c2] += cluster[c1]
        cluster[c1] = c2


def find(cluster, x):
    if cluster[x] is None:
        return x
    if cluster[x] < 0:
        return x
    cluster[x] = find(cluster, cluster[x])
    return cluster[x]
