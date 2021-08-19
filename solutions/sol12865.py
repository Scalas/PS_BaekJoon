import sys

input = sys.stdin.readline


# 12865 평범한 배낭
# 흔히 Knapsack(냅색)문제라고 불리는 배낭의 제한무게를 지키며 물건을 넣을 때 그 가치의 합의 최댓값을 구하는 문제
# 물건을 하나 넣을 때마다 그 물건으로 인해 생기는 경우의 수(무게)별 가치의 합의 최댓값을 추가, 갱신해나간다
# 모든 물건에 대해 갱신이 끝났을 때, 모든 경우의 수의 가치의 합 중 최댓값이 답이된다.
def sol12865():
    n, k = map(int, input().split())
    # 가치 : 무게 쌍의 딕셔너리
    dp = {0: 0}

    for i in range(n):
        # 물건의 무게, 가치
        w, v = map(int, input().split())

        # 딕셔너리의 업데이트 내역
        u = {}

        # 현재 딕셔너리에 있는 가치 : 무게 쌍들에 대해
        for value, weight in dp.items():
            # 물건을 추가하여 만들수있는 가치 : 무게 쌍을 구한 뒤
            nw, nv = w + weight, v + value

            # 기존에 같은 가치의 더 가벼운 케이스가 있거나 무게가 상한치인 k를 초과하지 않는다면 업데이트 내역에 추가
            if nw < dp.get(nv, k + 1):
                u[nv] = nw
        # 업데이트 내역 반영
        dp.update(u)

    # 딕셔너리에 남아있는 가치:무게 쌍은 모두 가방에 들어갈 수 있는 케이스
    # 그러므로 딕셔너리의 키값 리스트중 최댓값이 가치 합의 최댓값이 된다
    return max(dp.keys())
