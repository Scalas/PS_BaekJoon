import sys

input = sys.stdin.read


# 1135 뉴스 전하기
# 직원들은 자신의 직속부하에게 1분에 한명씩 전화를 할 수 있고
# 모든 직원이 자신보다 번호가 작은 한 명의 직속 상사만을 가질 때(트리구조)
# 0번 직원부터 시작하여 모든 직원이 전화를 받아 뉴스를 전달받을 때 까지 걸리는 최소시간을 구하는 문제
def sol1135():
    n, *p = map(int, input().split())
    g = [[] for _ in range(n)]
    for i in range(1, n):
        g[p[i]].append(i)

    # cur 번째 직원의 하위에 속한 모든 직원들이 소식을 듣는데 걸리는 최소시간
    def dfs(cur):
        # 최고 말단 직원은 더이상 알릴 직원이 없기에 0분이 걸림
        if not g[cur]:
            return 0

        res = 0
        # 직속 부하들이 각자 자신의 부하직원들에게 소식을 알리는데 걸리는 최소시간을 내림차순 정렬
        childs = [dfs(nxt) for nxt in g[cur]]
        childs.sort(reverse=True)

        # 가장 오래걸리는 직원 순으로 전화를 걸 때 걸리는 최소시간중 최댓값이 모든 직원에게 알리는데 걸리는 최소시간
        for i in range(len(childs)):
            res = max(res, childs[i]+i+1)
        return res

    # 0번 직원이 자신의 부하 직원에게 소식을 알리는데 걸리는 최소시간 반환
    return dfs(0)
