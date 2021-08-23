import sys

input = sys.stdin.readline


# 2213 트리의 독립 집합
# 트리의 최대 독립집합의 크기와 최대 독립 집합을 구하는 문제
# 트리 동적 계획법 문제이다.
def sol2213():
    # 노드의 갯수
    n = int(input())

    # 노드의 가중치
    w = [0] + list(map(int, input().split()))

    # 트리 구성
    g = [[] for _ in range(n + 1)]
    for i in sys.stdin:
        u, v = map(int, i.split())
        g[u].append(v)
        g[v].append(u)

    # 각 노드를 루트로 하는 서브트리의 경우별 최대 독립 집합 크기
    # mis[<노드번호>][0] 은 해당 노드가 포함되지 않았을 경우를,
    # mis[<노드번호>][1] 은 해당 노드가 포함된 경우의 최대 독립집합의 크기를 의미한다
    mis = [[-1, -1] for _ in range(n + 1)]

    # mis의 값을 채우기 위한 탐색 함수
    def make_set(prev, cur, include):
        # 현재 노드가 아직 방문되지 않았을 경우
        if mis[cur][0] == -1:
            # 현재 노드가 독립집합에 포함되지 않은 경우와 포함된 경우의 최대 독립 집합 크기를 초기화
            mis[cur] = [0, w[cur]]

            # 현재 노드의 자식 노드 순회하며 최대 독립집합의 크기를 합산
            for nxt in g[cur]:
                if nxt != prev:
                    # 자식노드를 포함하지 않은 경우의 최대 독립 집합 크기
                    ninc = make_set(cur, nxt, 0)

                    # 자식노드를 포함한 경우의 최대 독립 집합 크기
                    inc = make_set(cur, nxt, 1)

                    # 현재 노드가 포함된 상태일 경우 자식노드는 포함되지 않은 경우만 고를 수 있다.
                    mis[cur][1] += ninc

                    # 현재 노드가 포함되지 않은 상태일 경우 자식노드는 모든 경우중 더 큰 값을 고를 수 있다.
                    mis[cur][0] += max(ninc, inc)
            # 현재 노드에서의 최대 독립 집합의 크기 중 요청받은 상태에 해당하는 값을 반환(포함/제외)
        return mis[cur][include]

    # 실제 최대 독립 집합을 구하기 위한 추적 함수
    def trace_set(prev, cur, include):
        # 반환할 실제 최대 독립 집합
        res = set()

        # 현재 노드가 독립 집합에 포함될 수 있으며
        # 현재 노드가 포함되는 경우가 포함되지 않는 경우보다 독립 집합의 크기가 커진다면
        # 최대 독립 집합에 현재 노드를 최대 독립 집합에 포함
        # 현재 노드가 독립집합에 포함되었기 때문에 자식노드들은 포함될 수 없음
        if include and mis[cur][1] > mis[cur][0]:
            res.add(cur)
            include = 0

        # 현재 노드가 최대 독립 집합에 포함되지 않는 경우
        # 다음 노드가 독립집합에 포함될 가능성이 있음
        else:
            include = 1

        # 현재 노드의 자식노드를 순회
        # 각 자식노드를 루트로 하는 서브트리의 최대독립집합을 반환할 최대 독립집합에 합한다.
        for nxt in g[cur]:
            if nxt != prev:
                res |= trace_set(cur, nxt, include)

        # 최대 독립 집합 반환
        return res

    size, subset = 0, None
    # 루트 노드로 삼을 1번 노드가 포함된 경우와 포함되지 않은 경우중 큰 쪽을 선택
    if make_set(0, 1, 0) > make_set(0, 1, 1):
        size = make_set(0, 1, 0)
        subset = trace_set(0, 1, 0)
    else:
        size = make_set(0, 1, 1)
        subset = trace_set(0, 1, 1)

    # 최대 독립 집합의 크기와 최대 독립집합을 오름차순 정렬한 결과를 반환
    return str(size) + '\n' + ' '.join(map(str, sorted(subset)))


if __name__ == '__main__':
    print(sol2213())