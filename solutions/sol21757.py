import sys

input = sys.stdin.readline


# 21757 나누기
# n개의 정수로 이루어진 수열을 합이 같은 네 개의 구간으로 나누는 경우의 수를 구하는 문제
def sol21757():
    n = int(input())
    seq = list(map(int, input().split()))

    # 전체 합
    total = sum(seq)

    # 전체 합이 4로 나누어 떨어지지 않는다면 가능한 경우의 수가 없음
    if total % 4:
        return 0

    # 전체 합의 절반, 1/4
    half = total // 2
    quarter = half // 2

    # front[i]는 i이하의 지점중 맨 앞에서부터의 누적합이 quarter인 지점의 갯수
    # back[i]는 i이상의 지점중 맨 뒤에서부터의 누적합이 quarter인 지점의 갯수
    # center는 맨 앞에서의 누적합이 절반이 되는 지점들
    front = [0] * (n + 1)
    back = [0] * (n + 1)
    center = []
    # 수열의 누적합
    f, b = 0, 0
    for i in range(n):
        front[i] = front[i-1]
        back[n-i-1] = back[n-i]
        f += seq[i]
        if f == half:
            center.append(i)
        if f == quarter:
            front[i] += 1
        b += seq[n-i-1]
        if b == quarter:
            back[n-i-1] += 1

    # 모든 center에 대해 좌측의 quarter 구간과 우측의 quarter 구간의 수를
    # 곱한 값을 더하면 모든 경우의 수를 구할 수 있음
    answer = 0
    for c in center:
        # c를 중심(2번째 구간의 끝)으로 할 때 4개의 구간으로 나눌 수 없다면 스킵
        if c == 0 or c >= n-2:
            continue

        answer += front[c-1] * back[c+2]

    return answer
