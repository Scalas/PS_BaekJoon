import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


# 1766 문제집
# 문제집의 1~N까지의 문제를 풀 순서를 다음 세가지 조건에 따라 정하는 문제
# 1. N개의 문제는 모두 풀어야한다
# 2. 먼저 푸는 것이 좋은 문제가 있는 문제는 먼저 푸는 것이 좋은 문제를 반드시 먼저 풀어야 한다.
# 3. 가능하면 쉬운 문제부터 풀어야 한다. (문제 번호가 낮을수록 난이도가 낮다)
# 위상정렬과 heap 을 사용하여 해결 가능한 문제
def sol1766():
    # 문제의 갯수 n, 먼저 푸는게 좋은 문제의 정보의 갯수 m
    n, m = map(int, input().split())

    # 그래프, 진입 차수 테이블 생성
    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        g[a].append(b)
        degree[b] += 1

    # 최초에 진입 차수가 0인 노드(문제)를 큐에 담는다
    q = [i for i in range(1, n + 1) if not degree[i]]

    # 큐를 heapq로 변환
    # Python의 heapq는 기본적으로 최소 힙이기 때문에
    # 더 작은 숫자, 즉 더 쉬운 문제부터 뽑게된다.
    heapify(q)

    # 정렬 결과 리스트
    answer = []

    # 위상 정렬 실행
    # 기존의 방식과 같지만 큐에서 값을 꺼내고 다시 넣는 동작을
    # heappop 과 heappush를 사용하여 수행한다.
    # 이것으로 매번 가능하면 가장 쉬운 문제를 해결하는 3번 조건을 만족시킨다.
    while q:
        cur = heappop(q)
        answer.append(cur)
        for c in g[cur]:
            degree[c] -= 1
            if not degree[c]:
                heappush(q, c)

    # 출력 조건에 따라 정답 리스트 반환
    return ' '.join(map(str, answer))
