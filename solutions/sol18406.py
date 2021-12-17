import sys

input = sys.stdin.readline


# 18406 럭키 스트레이트
# 주어진 짝수자릿수의 숫자의 왼쪽과 오른쪽 절반의 자릿수의 합이 같다면 LUCKY 다르다면 READY를 출력하는 문제
def sol18406():
    n = input().rstrip()
    a, b = 0, 0
    for i in range(len(n)//2):
        a += int(n[i])
    for i in range(len(n)//2, len(n)):
        b += int(n[i])
    return 'LUCKY' if a == b else 'READY'
