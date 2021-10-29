import sys

input = sys.stdin.readline


# 13301 타일 장식물
# 1부터 시작하여 피보나치 수열에 따라 변의 길이가 늘어나는 정사각형을 나선형으로 이어붙여나갈 때
# n번째 정사각형까지 더한 상태의 전체 타일의 둘레길이를 구하는 문제
# fibo[n] * 2 + fibo[n+1] * 2 를 구하면 된다.
def sol13301():
    a, b = 1, 1
    for _ in range(int(input())-1):
        a, b = b, a+b
    return a*2 + b*2
