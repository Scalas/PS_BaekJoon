import sys

input = sys.stdin.readline


# 1010 다리놓기
# 강 서쪽과 동쪽의 도시들을 연결하는 다리를 놓는 문제
# 서쪽의 도시는 동쪽의 도시보다 적거나 같으며 다리는 서쪽의 도시 갯수만큼 놓아야 한다
# 다리는 서로 교차될 수 없다
# 즉, 서쪽의 도시가 n, 동쪽의 도시가 m일 때, c(m, n)을 구하면 되는 이항계수 문제이다.


# 이항계수를 구하는 다른 방법에 대해서는 11051번 문제에서 다루었기에
# 여기서는 간단하게 팩토리얼을 사용한 방법으로 풀었다.
def sol1010():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        h, l = 1, 1
        for i in range(n):
            h *= m - i
            l *= n - i
        print(h // l)

