from sys import stdin


# 1934 최소공배수
# 두 수의 최소공배수를 구하는 문제
# 유클리드 알고리즘으로 최대공약수를 구해 두 수의 곱에서 나누는것으로 해결 가능하다
def sol1934():
    answer = []
    stdin.readline()
    for i in stdin:
        n, m = map(int, i.split())
        if n < m:
            n, m = m, n
        gcd = [n, m]
        while gcd[1] != 0:
            gcd = [gcd[1], gcd[0] % gcd[1]]
        answer.append(str(n * m // gcd[0]))
    print('\n'.join(answer))
