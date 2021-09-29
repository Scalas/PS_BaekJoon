import sys

input = sys.stdin.readline


# 11057 오르막 수
# 1 <= n <= 1000 인 정수 n 이 주어졌을 때
# n 자리의 정수 중 자릿수가 이전 자릿수와 같거나 큰 수 (ex: 1112233) 의 갯수를 구하는 문제
def sol11057():
    # 자릿수
    n = int(input())

    # 마지막 자릿수가 0~9 인 오르막 수 의 갯수
    # 처음에는 0~9가 모두 하나씩 올 수 있기 때문에 1로 초기화
    digit = [1] * 10

    # 자릿수가 늘어날 때마다 마지막 자릿수가 k 인 오르막 수의 갯수는
    # 마지막 자릿수가 k보다 작은 오르막 수의 총 갯수가 된다.
    # digit 리스트에 대해 누적합 연산을 n-1 번 수행한 뒤 digit 의 값을 모두 더하면
    # n 자리 정수 중 오르막 수 의 갯수를 구할 수 있다.
    for i in range(1, n):
        for j in range(9):
            digit[j+1] += digit[j]
    return sum(digit) % 10007
