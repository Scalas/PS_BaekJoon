import sys

input = sys.stdin.readline


# 2252 줄 세우기
# 학생의 수와 키를 비교한 결과가 주어졌을 때 학생들을 키순서로 정렬하는 문제
# 위상정렬을 사용하여 간단하게 해결 가능한 문제이다.
def sol2252():
    # 학생의 수 n, 비교 결과의 수 m
    n, m = map(int, input().split())

    # 학생을 노드로, 비교 결과를 간선으로 하여 그래프로 표현
    # 각 노드(학생)의 진입 차수 테이블을 생성
    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        degree[b] += 1
        g[a].append(b)

    # 진입 차수가 0인 모든 노드를 큐에 삽입
    q = [i for i in range(1, n + 1) if not degree[i]]

    # 정렬 결과 리스트
    answer = []

    # 큐가 빌 때 까지
    while q:
        nq = []
        # 큐에서 노드를 하나씩 꺼내 정렬 결과 리스트 answer 에 삽입
        # 해당 노드로부터 뻗은 간선을 제거하고 진입 차수를 갱신
        # 그 결과 진입 차수가 0이 된 노드를 모두 큐에 삽입
        for num in q:
            answer.append(num)
            for child in g[num]:
                degree[child] -= 1
                if degree[child] == 0:
                    nq.append(child)
        q = nq

    # 출력 형식에 맞춰 정렬 결과를 반환
    return ' '.join(map(str, answer))
