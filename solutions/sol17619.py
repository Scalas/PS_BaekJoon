import sys

input = sys.stdin.readline


# 17619 개구리 점프
# 통나무 n개의 높이와 통나무가 연결하는 두 x좌표가 1~n번까지 번호순으로 주어질 때
# 두 통나무의 번호에 대해 통나무 사이에 이동이 가능한지 여부를 구하는 문제
def sol17619():
    n, q = map(int, input().split())

    # 통나무를 좌측 좌표순으로 정렬
    log = []
    for i in range(1, n+1):
        x1, x2, y = map(int, input().split())
        log.append([x1, x2, i])
    log.sort()

    # 통나무가 속하는 그룹
    group = [-1] * (n+1)

    # 그룹번호, 이전 오른쪽 x좌표
    gn, px = 0, -1

    for i in range(n):
        x1, x2, num = log[i]
        # 왼쪽 좌표가 이전 그룹의 오른쪽 좌표보다 작거나 같다면 그 그룹에 속함
        if x1 <= px:
            group[num] = gn
            # 오른쪽 x좌표 갱신
            px = max(px, x2)

        # 그렇지 않다면 현재 좌표를 기준으로 새 그룹을 생성
        else:
            px = x2
            gn += 1
            group[num] = gn

    # 두 통나무의 그룹이 같은지 확인
    answer = []
    for _ in range(q):
        x1, x2 = map(int, input().split())
        if group[x1] == group[x2]:
            answer.append(1)
        else:
            answer.append(0)

    return '\n'.join(map(str, answer))
