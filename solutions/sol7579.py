import sys

input = sys.stdin.readline


# 7579 앱
# M 만큼의 메모리를 확보하기 위해 들어가는 최소코스트를 구하는 문제
# 냅색 문제의 응용이지만 다른점은 넣을 항목의 제한조건이 무게(K)이하가 아니라 메모리(M)이상을 넣어야한다는 점이다
# memory 를 key 값으로 딕셔너리를 생성하면 메모리초과, 시간초과 문제가 발생하기에
# 범위가 작은 cost 를 key 값으로 사용하여 딕셔너리를 생성한다
def sol7579():
    # 앱의 갯수 n,  확보해야할 메모리 크기 m
    n, m = map(int, input().split())

    # 각 앱이 차지하는 메모리 크기
    memory = list(map(int, input().split()))

    # 각 앱을 종료하는데 들어가는 비용
    cost = list(map(int, input().split()))

    # 앱을 종료하는데 드는 비용 총합 : 확보할 수 있는 메모리 총량
    dp = {0: 0}

    # m 만큼의 메모리를 확보하기 위해 필요한 최소비용
    answer = float('inf')

    # 각 앱을 종료하는 것으로 확보할 수 있는 메모리 총량을 딕셔너리에 추가
    for app in range(n):
        u = {}
        for co, mem in dp.items():
            co += cost[app]
            mem += memory[app]
            if mem >= m:
                answer = min(answer, co)
            elif dp.get(co, 0) < mem:
                u[co] = mem
        dp.update(u)

    # 필요한 최소비용을 반환
    return answer
