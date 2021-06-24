import sys

input = sys.stdin.read


# 1003 피보나치 함수
# 재귀형태로 구성된 피보나치 함수를 실행했을 때 출력되는 0과 1의 갯수를 구하는문제
# 1의 출력횟수는 입력에 해당하는 피보나치수와 같으며
# 0의 출력횟수는 그 다음 피보나치 수에서 입력에 해당하는 피보나치 수를 뺀 것과 같다
# 처음부터 0과 1의 횟수를 모두 동적계획법으로 구하는 방식도 가능하다
def sol1003():
    fibo = [0] * 42
    fibo[1] = 1
    for i in range(2, 42):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    n, *case = map(int, input().split())
    answer = [f'{fibo[c + 1] - fibo[c]} {fibo[c]}' for c in case]
    print('\n'.join(answer))
