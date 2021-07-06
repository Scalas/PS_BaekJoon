from sys import stdin


# 7579 앱
# M 만큼의 메모리를 확보하기 위해 들어가는 최소코스트를 구하는 문제
# 냅색 문제의 응용이지만 다른점은 넣을 항목의 제한조건이 무게(K)이하가 아니라 메모리(M)이상을 넣어야한다는 점이다
# memory 를 key 값으로 딕셔너리를 생성하면 메모리초과, 시간초과 문제가 발생하기에
# 범위가 작은 cost 를 key 값으로 사용하여 딕셔너리를 생성한다
def sol7579():
    n, m = map(int, stdin.readline().split())
    dp = {0:0}
    answer = float('inf')
    for mm, cc in zip(*[map(int, line.split()) for line in stdin.read().splitlines()]):
        u = {}
        for cost in dp:
            nc, nm = cc + cost, mm + dp[cost]
            if dp.get(nc, 0) < nm:
                u[nc] = nm
                if nm >= m:
                    answer = min(answer, nc)
        dp.update(u)
    print(answer)

