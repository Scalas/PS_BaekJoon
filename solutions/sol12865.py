from sys import stdin


# 12865 평범한 배낭
# 흔히 Knapsack(냅색)문제라고 불리는 배낭의 제한무게를 지키며 물건을 넣을 때 그 가치의 합의 최댓값을 구하는 문제
# 물건을 하나 넣을 때마다 그 물건으로 인해 생기는 경우의 수(무게)별 가치의 합의 최댓값을 추가, 갱신해나간다
# 모든 물건에 대해 갱신이 끝났을 때, 모든 경우의 수의 가치의 합 중 최댓값이 답이된다.

# 예를들어 n = 2, k = 5 이고 후보 물건이 (3, 6), (2, 8) 일 때
# (3, 6) 이 들어오면 dp = {0:0, 3:6}  (초기값 0:0 은 물건을 넣을 수 없거나 각각 하나만 넣을 경우를 위함)
# (2, 8) 이 들어오면 dp = {0:0, 3:6, 2:8, 5:14} 가 된다
# dp 의 값의 모음 (0, 6, 8, 14) 중 최댓값인 14가 답이된다
def sol12865():
    n, k, *items = map(int, stdin.read().split())
    dp = {0:0}
    for i in range(0, n * 2, 2):
        w, v = items[i], items[i+1]
        if v > 0 and w <= k:
            update = {}
            for key, value in dp.items():
                weight = key + w
                if weight <= k and value + v > dp.get(weight, 0):
                    update[weight] = value + v
            dp.update(update)
    print(max(dp.values()))
