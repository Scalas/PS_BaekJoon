import sys

input = sys.stdin.readline


# 9372 상근이의 여행
# 가장 적은 갯수의 간선으로 모든 정점을 연결하는 문제
# N개의 정점을 모두 연결하려면 최소 N-1 개의 간선이 필요하다는 사실을 기억하면 쉽게 해결 가능한 문제
def sol9372():
    answer = []
    for _ in range(int(input())):
        n, m = map(int, input().split())
        for _ in range(m):
            input()
        answer.append(n - 1)
    print('\n'.join(map(str, answer)))
