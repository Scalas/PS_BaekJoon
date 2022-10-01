import sys

input = sys.stdin.readline


# 16721 Structure of Balanced
# n개의 노드간의 연결관계 행렬이 주어졌을 때
# 주어진 두 노드들의 관계를 출력하는 문제
# 메모리 제한을 해결하기 위해 그래프를 string 형태로 저장하여 인덱스를 계산하도록함
def sol16721():
    n = int(input())
    g = ''
    for i in range(n):
        g += ''.join(input().split())

    for _ in range(int(input())):
        u, v = map(int, input().split())
        print(g[u * n + v])
