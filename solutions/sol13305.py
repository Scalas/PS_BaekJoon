import sys

input = sys.stdin.read


# 13305 주유소
# 직선상에 도시와 주유소들이 있을 때 맨 왼쪽 도시에서 맨 오른쪽 도시로 이동하는데 드는 기름값의 최소비용을 찾는 문제
def sol13305():
    n, c, p = input().splitlines()
    n, c, p = int(n), list(map(int, c.split())), list(map(int, p.split()))

    price = float('inf')
    answer = 0
    for i in range(n - 1):
        price = min(price, p[i])
        answer += c[i] * price
    print(answer)
