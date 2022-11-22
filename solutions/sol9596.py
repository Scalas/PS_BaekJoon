import sys

input = sys.stdin.readline
MOD = 21092013


# 9596 바이너리 트리
# 크기가 무한대인 바이너리 트리에서
# L(Left), R(Right), U(Parent) 로 이동할 수 있고
# 이동 명령을 담은 문자열 S, T 가 주어졌을 때,
# S의 명령대로 이동한 뒤, T의 명령에 따라 이동했을 때 이동을 끝낼 수 있는 노드의 갯수를 구하는 문제
# 단, T는 명령을 생략할 수 있으며(순서는 바꿀 수 없다) 노드의 갯수는 21092013으로 나눈 나머지를 구한다.
# 또한, 루트 노드에서 U 이동시에는 이동 결과도 루트노드이다.
def sol9596():
    answers = []

    for case_idx in range(int(input())):
        s = input().rstrip()
        t = input().rstrip()

        # S 이동을 실시
        # start_node 의 마지막 원소는 S이동을 마친 후 T 이동을 시작할 시작 노드의 상태를 나타냄
        # -1일 경우 시작노드는 루트노드와 같으며
        # 0일 경우 부모 노드의 좌측 자식 노드, 1일 경우 부모 노드의 우측 자식 노드이다.
        start_node = [-1]
        for c in s:
            if c == 'U':
                if start_node[-1] != -1:
                    start_node.pop()
            elif c == 'L':
                start_node.append(0)
            else:
                start_node.append(1)

        n = len(t)
        # 0 = 양측 자식노드가 방문 가능한 노드
        # 1 = 좌측 자식노드만 방문 가능한 노드
        # 2 = 우측 자식노드만 방문 가능한 노드
        # 3 = 아무 자식노드도 방문 불가능한 노드
        node = [1, 0, 0, 0]
        for i in range(n):
            # 위쪽으로 이동시
            if t[i] == 'U':
                # 시작 노드가 루트 노드일 경우
                # 아무 노드도 늘어나지 않음
                if start_node[-1] == -1:
                    continue
                # 시작 노드가 부모의 우측 자식노드일 경우
                # 시작 노드의 부모노드. 즉, 좌측 자식노드만 방문 가능한 노드가 증가
                if start_node[-1] == 1:
                    node[1] = (node[1] + 1) % MOD
                # 시작 노드가 부모의 좌측 자식노드일 경우
                # 시작 노드의 부모노드. 즉, 우측 자식노드만 방문 가능한 노드가 증가
                else:
                    node[2] = (node[2] + 1) % MOD
                start_node.pop()

            # 좌측으로 이동시
            elif t[i] == 'L':
                # 양쪽 자식노드 모두 방문 가능한 노드들이
                # 우측 자식노드만 방문 가능한 노드로 전환되고
                # 그만큼 양쪽 자식노드 모두 방문 가능한 노드가 증가
                # 그러므로 양쪽 노드 모두 방문 가능한 노드 갯수는 그대로
                node[2] = (node[2] + node[0]) % MOD

                # 좌측 자식노드만 방문 가능한 노드들이
                # 양쪽 자식노드 모두 방문 불가능한 노드로 전환되고
                # 그만큼 양쪽 자식노드 모두 방문 가능한 노드가 증가
                node[3] = (node[3] + node[1]) % MOD
                node[0] = (node[0] + node[1]) % MOD
                node[1] = 0
                continue

            # 우측으로 이동시
            else:
                # 양쪽 자식노드 모두 방문 가능한 노드들이
                # 좌측 자식노드만 방문 가능한 노드로 전환되고
                # 그만큼 양쪽 자식노드 모두 방문 가능한 노드가 증가
                # 그러므로 양쪽 노드 모두 방문 가능한 노드 갯수는 그대로
                node[1] = (node[1] + node[0]) % MOD

                # 우측 자식노드만 방문 가능한 노드들이
                # 양쪽 자식노드 모두 방문 불가능한 노드로 전환되고
                # 그만큼 양쪽 자식노드 모두 방문 가능한 노드가 증가
                node[3] = (node[3] + node[2]) % MOD
                node[0] = (node[0] + node[2]) % MOD
                node[2] = 0

        answers.append(f'Case {case_idx + 1}: {sum(node) % MOD}')

    return '\n'.join(answers)
