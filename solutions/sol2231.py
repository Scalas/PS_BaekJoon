import sys


# 2231 분해합
# 자기 자신과 자신의 각 자릿수를 모두 더해서 n이 되는 가장 작은 수를 구하는 문제
def sol2231():
    n = sys.stdin.readline()
    d = len(n) - 1  # n의 자릿수
    n = int(n)

    # 생성자는 n에서 자릿수만큼 9를 뺀 것보다 작을 수 없음
    for num in range(max(n - d * 9, 1), n):
        if num + sum(map(int, str(num))) == n:
            return num

    return 0
