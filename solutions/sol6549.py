import sys
from collections import defaultdict

input = sys.stdin.readline


# 6549 히스토그램에서 가장 큰 직사각형
# 너비가 1인 서로다른 높이의 직사각형으로 이루어진 히스토그램에서
# 만들 수 있는 가장 큰 넓이의 직사각형을 찾는 문제


# 분할 정복을 사용한 방법
# 직사각형의 갯수가 N 일때, max_rect 호출에 의한 복잡도 O(logN)
# max_rect마다 정렬을 사용하기 떄문에 O(NlogN)
# O(N(logN)^2) 의 복잡도로 해결 가능하다
def sol6549():
    answer = []
    while True:
        args = list(map(int, input().split()))

        # 마지막 입력
        if not args[0]:
            break

        n, *hist = args
        # 전체범위에 대해 가장 큰 직사각형의 넓이를 구한다
        answer.append(max_rect(hist, 0, n-1))
    return '\n'.join(map(str, answer))


# left부터 right 까지의 히스토그램에 대한 가장 큰 직사각형의 넓이를 구하는 함수
def max_rect(hist, left, right):
    # 한칸짜리 히스토그램이라면 높이를 반환
    if left == right:
        return hist[left]

    # 중간위치
    mid = (left + right) // 2

    # 중간지점을 기준으로 좌우로 뻗어나가며
    # 높이가 감소한다면 그대로, 증가한다면 이전의 높이와 같게하여
    # 높이별 갯수를 딕셔너리로 카운팅
    curv = 0
    d = defaultdict(int)
    d[hist[mid]] += 1
    d[hist[mid+1]] += 1
    s, e = mid-1, mid+2
    sh, eh = hist[mid], hist[mid+1]
    while s >= left:
        if hist[s] < sh:
            sh = hist[s]
        d[sh] += 1
        s -= 1
    while e <= right:
        if hist[e] < eh:
            eh = hist[e]
        d[eh] += 1
        e += 1

    # 딕셔너리의 키로 사용된 높이를 오름차순으로 정렬
    # 초기 직사각형의 갯수는 범위 전체(e - s - 1)
    # 가장 낮은높이부터 (높이 * 직사각형 갯수)로 최대 직사각형 넓이를 갱신한 뒤
    # 사용한 높이의 갯수만큼을 직사각형 갯수에서 감산하기를 반복
    cnt = e-s-1
    for h in sorted(d.keys()):
        curv = max(curv, h*cnt)
        cnt -= d[h]

    # 위의 과정을 통해 구한 curv 값과 중간지점 mid를 기준으로
    # 좌, 우로 max_rect를 재귀호출한 결과들중 최댓값을 반환한다.
    return max(curv, max_rect(hist, left, mid), max_rect(hist, mid+1, right))


# 스택을 사용한 방법
# N개의 직사각형을 스택에 넣고 빼는데 2N
# O(N)의 시간복잡도로 해결 가능
def sol6549_2():
    answer = []
    while True:
        args = list(map(int, input().split()))

        # 마지막 입력
        if not args[0]:
            break

        n, *hist = args
        # 최대 직사각형 넓이
        maxv = 0
        st = [[0, 0]]
        hist.append(0)

        # 히스토그램의 직사각형을 순차적으로 추가
        for h in hist:
            cnt = 0
            # 추가된 직사각형보다 높이가 큰 직사각형을 모두 pop
            # pop된 직사각형은 자신의 높이 * 갯수(넓이)로 최대 maxv를 갱신
            # pop된 직사각형의 갯수만큼 cnt 증가
            while st and h < st[-1][0]:
                ph, c = st.pop()
                maxv = max(maxv, ph * (cnt+c))
                cnt += c

            # 만약 자신과 같은높이의 직사각형이 존재한다면 cnt + 1만큼 같은높이의 직사각형의 갯수를 증가
            if h == st[-1][0]:
                st[-1][1] += (cnt+1)
            # 새로 추가한 직사각형의 높이가 이전 직사각형보다 크다면
            # 자신의 높이의 직사각형을 cnt + 1개 추가
            else:
                st.append([h, cnt+1])

        answer.append(maxv)

    return '\n'.join(map(str, answer))
