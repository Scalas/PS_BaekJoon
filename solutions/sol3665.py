import sys

input = sys.stdin.readline


# 3665 최종 순위
# 작년의 팀들의 순위, 올해 상대적 순위가 변경된 팀의 순서쌍이 주어졌을 때, 올해 팀들의 순위를 구하는 문제.
# 간선을 직접 정의하여 위상정렬을 수행해야 하는 문제이다.
def sol3665():
    # 케이스별 정렬 결과 리스트
    answer = []

    for t in range(int(input())):
        # 팀의 수(노드의 수)
        n = int(input())

        # 작년 순위에 따라 그래프와 차수 테이블 생성
        g = [set() for _ in range(n + 1)]
        degree = [0] * (n + 1)
        teams = list(map(int, input().split()))
        for i in range(n):
            a = teams[i]
            for j in range(i + 1, n):
                b = teams[j]
                g[a].add(b)
                degree[b] += 1

        # 변경된 순위에 따라 그래프와 차수 테이블 수정
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())

            # 보다 낮은 순위였던 쪽이 a가 되게 한다
            if a not in g[b]:
                a, b = b, a

            g[b].discard(a)
            g[a].add(b)
            degree[a] -= 1
            degree[b] += 1

        # 정렬 결과
        res = []

        # 위상 정렬 수행
        q = [i for i in range(1, n + 1) if not degree[i]]
        while q:
            nq = []
            for num in q:
                res.append(num)
                for child in g[num]:
                    degree[child] -= 1
                    if not degree[child]:
                        nq.append(child)
            q = nq

        # 사이클이 발견된 경우 -> 일관성이 없어 정렬이 불가능한 경우
        if len(res) != n:
            answer.append('IMPOSSIBLE')

        # 정렬이 정상적으로 수행된 경우
        else:
            answer.append(' '.join(map(str, res)))

    # 출력 형식에 맞춰 정렬 결과 반환
    return '\n'.join(answer)
