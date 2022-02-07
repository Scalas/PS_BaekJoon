import sys

input = sys.stdin.readline


# 14267 회사 문화 1
# 1번부터 n번 사원의 직속상사/부하 관계와 최초에 칭찬을 받은 사원과 받은 칭찬의 수치가 주어지고
# 칭찬을 받은 사원이 자신의 직속부하에게 내리칭찬을 해나간다고 할 때
# 각 직원들이 받게될 칭찬의 수치를 구하는 문제
def sol14267():
    n, m = map(int, input().split())
    org = [*map(lambda x:int(x)-1, input().split())]
    praise = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        praise[u-1] += v
    for i in range(1, n):
        praise[i] += praise[org[i]]
    return ' '.join(map(str, praise))
