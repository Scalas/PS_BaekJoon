import sys

input = sys.stdin.readline


# 2024 선분 덮기
# 선분들의 왼쪽과 오른쪽 좌표들이 주어지고 덮어야할 구간의 오른쪽 값 m이 주어졌을 때
# 구간 [0, m] 을 덮기 위해 필요한 선분의 최소 갯수를 구하는 문제
# 만약 덮을 수 없다면 0을 반환
def sol2024():
    m = int(input())

    # 선분의 좌표를 입력받은 후 왼쪽좌표 기준으로 정렬
    lines = []
    while True:
        l, r = map(int, input().split())
        if l == r == 0:
            break
        lines.append([l, r])
    lines.sort()

    i = 0
    nxt = 0
    cnt = 0
    for l, r in lines:
        # 덮어야할 구간의 가장 왼쪽 좌표보다 나중에 시작하는 선분일 경우
        # 다음 구간을 덮기 위한 선분으로 판정
        if l > i:
            # 이전에 덮은 구간과 이어지지 않는다면 선을 덮을 방법이 없음
            if nxt < l:
                return 0
            # 이전에 덮은 구간과 이어진다면 선분 갯수를 하나 늘리고
            # 이전에 덮은 구간의 가장 오른쪽 좌표로 덮어야할 구간의 가장 왼쪽 좌표를 갱신
            cnt += 1
            i = nxt

            # i가 이미 m이상이라면 선분 갯수 바로 반환
            if i >= m:
                return cnt

        # 선분으로 덮어질 구간의 끝을 갱신
        nxt = max(nxt, r)

    # 아직 반영되지 않은 선분이 있다면 선분의 갯수를 추가하고 덮은 구간의 가장 오른쪽 좌표 갱신
    if nxt > i:
        i = nxt
        cnt += 1

    # 마지막 선분까지 사용했을 때 선분을 덮을 수 없다면 0을 반환
    # 덮을 수 있다면 사용된 선분의 갯수 반환
    return 0 if i < m else cnt
