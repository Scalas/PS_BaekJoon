import sys

input = sys.stdin.readline


# 1029 그림 교환
# 그림을 한 번도 이 그림을 산적이 없는 사람에게 자신이 사온 가격과 같거나 더 비싸게 팔 수 있고
# 0~n-1 번 까지의 사람이 서로 그림을 사고파는 가격이 주어졌을 때 그림을 샀던적이 있는 사람의 수의 최댓값을 구하는 문제
# 단, 0번 사람은 가격 0에 그림을 사왔다고 가정한다.
def sol1029():
    n = int(input())
    g = [[*map(int, list(input().rstrip()))] for _ in range(n)]
    bit = [1 << i for i in range(n+1)]

    # 그림의 소유자는 0번이고 소유이력이 있는 사람도 0번뿐이며 마지막 거래가도 0인 상태(초기상태)
    q = {(0, 1, 0)}

    # 거래 횟수
    answer = 0
    while q:
        nq = set()
        # 거래횟수가 answer+1일 때 그림을 가진사람이 있다면 거래횟수 증가
        answer += 1
        for cur, state, price in q:
            for nxt in range(n):
                # nxt 번째 사람과 거래할 경우 상태와 최종거래가
                nstate, nprice = state | bit[nxt], g[cur][nxt]

                # 이미 그림을 구매한 적이 있는 사람이거나 최종 거래가보다 낮은 가격에 팔아야할 경우 거래하지 않음
                if state == nstate or nprice < price:
                    continue

                # set 에 해당 케이스 추가(중복은 자동으로 제거)
                nq.add((nxt, nstate, nprice))
        q = nq

    # 최대 거래횟수 반환
    return answer
