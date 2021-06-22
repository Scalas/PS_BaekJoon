from sys import stdin

input = stdin.readline


# 1010 다리놓기
# 강 서쪽과 동쪽의 도시들을 연결하는 다리를 놓는 문제
# 서쪽의 도시는 동쪽의 도시보다 적거나 같으며 다리는 서쪽의 도시 갯수만큼 놓아야 한다
# 다리는 서로 교차될 수 없다
# 즉, 서쪽의 도시가 n, 동쪽의 도시가 m일 때, c(m, n)을 구하면 되는 이항계수 문제이다.


# 첫 번째 시도
# 단순히 팩토리얼을 사용한 풀이
def sol1010():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        h, l = 1, 1
        for i in range(n):
            h *= m - i
            l *= n - i
        print(h // l)


# 두 번째 시도
# 테스트 케이스가 여러개 주어지는 타입의 문제이기에
# 동적계획법을 사용하여 최대범위까지 이항계수를 구해두고 출력하는 풀이
# n, m의 범위가 커지고 테스트케이스가 많아질수록 첫 번째 풀이와 유의미한 속도 차이를 보일 수 있음
def sol1010_2():
    dp = [[0] * 30 for _ in range(30)]
    for i in range(1, 30):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(2, 30):
        for j in range(1, 30):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    stdin.readline()
    answer = []
    for i in stdin:
        n, m = map(int, i.split())
        answer.append(str(dp[m][n]))

    print('\n'.join(answer))
