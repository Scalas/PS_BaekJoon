import sys

input = sys.stdin.readline


# 2230 수 고르기
# 수열 A 에서 고른 두 수의 차 중 m 이상이면서 가장 작은 값을 구하는 문제
# 단, 같은 수를 두 번 고를 수 있다.
def sol2230():
    n, m = map(int, input().split())
    seq = [int(input()) for _ in range(n)]

    # m이 0이라면 답은 항상 0 (같은 수를 두개 고르는 경우)
    if m == 0:
        return 0

    seq.sort()
    
    # 투 포인터를 사용하여 차가 처음으로 m 이상이 되는 모든 시점중 최솟값을 구함
    idx1 = idx2 = 0
    answer = float('inf')
    while idx2 < n:
        diff = seq[idx2] - seq[idx1]
        if diff >= m:
            answer = min(answer, diff)
            idx1 += 1
        else:
            idx2 += 1

    return answer
