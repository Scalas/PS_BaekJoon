import sys

input = sys.stdin.readline


# 10250 ACM 호텔
# n번째 손님의 방 호수 구하기 문제
# 호수는 n/h의 올림
# 층수는 n%h  (n%h가 0일경우 h)
def sol10250():
    answer = []
    for t in range(int(input())):
        h, w, n = map(int, input().split())
        addr = (n // h) + 1 + (n % h) * 100 if n % h != 0 else (n // h) + (h * 100)
        answer.append(str(addr))
    print('\n'.join(answer))
