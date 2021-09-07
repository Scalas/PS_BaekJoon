import sys

input = sys.stdin.readline


# 10266 시계 사진들
# 동일한 길이의 바늘 n 개를 가진 두 시계의 각 바늘이 9시방향과 이루는 각도가 순서없이 주어졌을 때
# 두 시계를 회전시켜 같은 시간을 가리키도록 할 수 있는지 구하는 문제.  각도의 단위는 1/1000도(degree)이다.
def sol10266():
    # 시계의 바늘 갯수
    n = int(input())

    # 두 시계의 바늘의 각도를 오름차순 정렬
    x = sorted(map(int, input().split()))
    y = sorted(map(int, input().split()))

    # 인접한 바늘끼리의 각도차 리스트를 구함
    a = ([x[(i + 1)] - x[i] for i in range(n - 1)] + [x[0] - (x[-1] - 360000)]) * 2
    b = [y[(i + 1)] - y[i] for i in range(n - 1)] + [y[0] - (y[-1] - 360000)]
    n, m = 2 * n, n

    # LPS 테이블 전처리
    lps = [0] * (m + 1)
    i = 0
    for j in range(1, m):
        while i > 0 and b[i] != b[j]:
            i = lps[i - 1]
        if b[i] == b[j]:
            i += 1
            lps[j] = i

    # KMP 알고리즘으로 문자열 탐색 시작
    i, j = 0, 0
    while i < n:
        if a[i] == b[j]:
            i += 1
            j += 1
            # 탐색에 성공했다면 같은 시각을 나타내도록 할 수 있음
            # 'possibe' 반환
            if j == m:
                return 'possible'
        else:
            if j == 0:
                i += 1
            j = lps[j - 1]

    # 모든 작업을 마칠동안 탐색에 성공하지 못했다면
    # 같은시각을 나타내도록 할 수 없음
    # 'impossible' 반환
    return 'impossible'
