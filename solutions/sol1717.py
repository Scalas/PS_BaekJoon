import sys

input = sys.stdin.readline


# 1717 집합의 표현
# 수의 집합을 트리의 형태로 표현하는 알고리즘인 유니온 파인드에 대해 알아보는 문제
def sol1717():
    n, m = map(int, input().split())
    # u[x] 가 음수이며 절댓값이 k일 때, x는 자신이 속한 트리(집합)의 루트노드이며
    # 그 안에 자신을 포함하여 k개의 노드가 있다.
    # 처음에는 모든 원소가 별도의 집합이기에 각자가 루트노드이며 집합에 자기자신만이 들어있기에 -1로 초기화한다.
    u = [-1] * (n + 1)

    answer = []
    # m 개의 연산 처리
    for _ in range(m):
        t, a, b = map(int, input().split())
        # 0 a b 형태의 명령어라면 a와 b가 같은 집합에 속해있는지 여부를 검사한다
        # find 함수는 수가 포함된 집합의 루트노드를 반환하기에 find 의 결과가 같다면 같은 트리에 속해있음을 알 수 있다.
        if t:
            answer.append('YES' if find(u, a) == find(u, b) else 'NO')
        # 1 a b 형태의 명령어라면 a와 b가 속한 집합을 합친다
        else:
            union(u, a, b)

    return '\n'.join(answer)


# 합집합 연산
def union(u, a, b):
    # a 와 b의 루트노드를 탐색
    a = find(u, a)
    b = find(u, b)

    # 두 수의 루트노드가 같지 않은경우 집합을 합친다.
    if a != b:
        # 두 집합 중 보다 크기가 큰쪽에 작은쪽을 붙여야 트리의 깊이를 줄일 수 있다.
        if u[a] < u[b]:
            u[a] += u[b]
            u[a] = b
        else:
            u[b] += u[a]
            u[b] = a


# x의 루트노드 탐색
def find(u, x):
    # x 자신이 루트노드라면 자신을 반환
    if u[x] < 0:
        return x
    # 재귀로 루트노드를 찾아 거슬러올라가며 부모노드를 갱신 후 부모노드(= 루트노드)를 반환한다
    # 다음에 다시 찾을떈 이 과정이 이미 끝나있기에 탐색이 빨라진다
    u[x] = find(u, u[x])
    return u[x]
