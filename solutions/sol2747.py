import sys

input = sys.stdin.readline


# 2748 피보나치 수 2
# n 번째 피보나치 수를 구하는 문제
# n이 90 이하의 자연수이기 때문에 동적계획법을 사용한 풀이로 해결 가능하다.
def sol2748():
    fibo, nxt = 0, 1
    for i in range(int(input())):
        fibo, nxt = nxt, fibo + nxt

    return fibo
