import sys

input = sys.stdin.readline


# 10986 나머지의 합
# n개의 수로 이루어진 수열의 부분연속구간중
# 합이 m으로 나누어떨어지는 구간의 갯수를 구하는 문제
def sol10986():
    n, m = map(int, input().split())
    seq = [0, *map(int, input().split())]

    # 합이 m으로 나누어떨어지는 연속부분구간의 갯수
    answer = 0

    # check_remain[i] 는 구간합의 나머지가 i일 때
    # 구간합이 m으로 나누어 떨어질 수 있는 경우의 수
    check_remain = [0] * m

    # 처음에는 나머지가 0일 때만 나누어떨어질 수 있음
    check_remain[0] = 1

    for i in range(1, n+1):
        # 수열의 i번째 수 까지의 누적합을 구합
        seq[i] += seq[i-1]

        # 누적합을 m으로 나눈 나머지
        r = seq[i] % m

        # 누적합을 m으로 나눈 나머지가 m으로 나누어 떨어질 수 있는 경우의 수 만큼 answer 증가
        answer += check_remain[r]

        # i 이후의 구간에서는 i까지의 누적합을 뺄 수 있기 때문에 나머지가 r인 경우에도
        # m으로 나누어 떨어질 수 있으므로 check_reamin[r] 값을 1 증가
        check_remain[r] += 1
        
    # m으로 나누어 떨어지는 모든 연속부분구간의 갯수를 반환
    return answer
