import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
full_visit = (1 << k)-1
inf = 10 ** 9


# 17406 배열 돌리기 4
# n * m 배열에 대해 연산 k가 주어졌을 때 이를 반영하는 순서에 따른 배열의 값의 최솟값을 구하는 문제
# 배열의 값은 배열의 각 열의 모든 요소의 합 중 최솟값을 의미한다.
# 연산은 r, c, s 의 형태로 주어지며 좌측 최상단 인덱스가 (r-s, c-s) 이고
# 우측 최하단 인덱스가 (r+s, c+s) 인 범위에 대해 회전연산을 수행하는 연산을 의미한다.
def sol17406():
    # 배열 초기상태
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 회전 연산 리스트
    rotate = [list(map(int, input().split())) for _ in range(k)]

    # 시작 연산을 선택하여 각 경우의 최소 배열값 중 최솟값을 반환
    answer = inf
    for i in range(k):
        answer = min(answer, dfs(arr, rotate, 1<<i, i))
    return answer


def dfs(arr, rotate, visited, selected):
    res = inf

    # 회전수행
    r, c, s = rotate[selected]
    nxt_arr = [arr[i][:] for i in range(len(arr))]
    rot(nxt_arr, r, c, s)

    # 모든 연산을 수행했다면 결과 반환
    if visited == full_visit:
        return min(map(sum, nxt_arr))

    # 다음 연산을 선택
    for i in range(k):
        if not (visited & 1 << i):
            res = min(res, dfs(nxt_arr, rotate, visited | (1<<i), i))

    # 다음 연산을 선택한 결과중 가장 큰 값을 반환
    return res


def rot(arr, r, c, s):
    lr, lc, rr, rc = r-s-1, c-s-1, r+s-1, c+s-1

    # 회전범위의 첫번째 요소 저장
    f = arr[lr][lc]

    # 왼쪽 가장자리 당기기
    for i in range(lr, rr):
        arr[i][lc] = arr[i+1][lc]

    # 아래쪽 가장자리 당기기
    for i in range(lc, rc):
        arr[rr][i] = arr[rr][i+1]

    # 오른쪽 가장자리 당기기
    for i in range(rr, lr, -1):
        arr[i][rc] = arr[i-1][rc]

    # 위쪽 가장자리 당기기
    for i in range(rc, lc, -1):
        arr[lr][i] = arr[lr][i-1]

    # 회전범위의 첫번째요소 위치에 넣어주기
    arr[lr][lc+1] = f

    # 정사각형 범위의 크기가 3 * 3 보다 클 때
    # 내부 범위에 대해 회전함수 재귀호출
    # 3 * 3일 경우에는 내부 범위가 1 * 1이기 때문에 호출할 필요 없음
    # 2 * 2일 경우에는 내부 범위가 존재하지 않기 때문에 호출할 필요 없음
    if s > 1:
        rot(arr, r, c, s-1)
