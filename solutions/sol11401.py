import sys

input = sys.stdin.readline

mod = 1000000007


# 11401 이항계수 3
# c(n, k)를 구하는 문제
# 기존 이항계수 문제들과 달리 n, k의 값이 400만까지 커지기때문에 동적계획법이나 완전탐색을 통한 방법은 시간초과 발생
# 페르마의 소정리나 확장 유클리드 방정식을 통해 풀 수 있다
# 여기서는 페르마의 소정리만 활용해서 풀어보았다
def sol11401():
    n, k = map(int, input().split())
    # k가 n의 절반을 넘어설 경우 n-k로 바꿔줌 ( c(n, k) = c(n, n-k) )
    if (k > n // 2):
        k = n - k
    global mod

    # fact(a, b) 가 a부터 b-1까지의 곱이라고 할 때
    # c(n, k)
    # = n! / (k! * (n-k)!)
    # = fact(n-k+1, n+1) / k!

    # 페르마의 소정리에 따라
    # c(n, k) % mod
    # = (fact(n-k+1, n+1) / k!) % mod
    # = fact(n-k+1, n+1) * (k! ^ (mod-2)) % mod
    print(fact(n - k + 1, n + 1) * pow(fact(1, k + 1), mod - 2) % mod)


# 분할정복을 활용하여 a**b를 구함
def pow(a, b):
    global mod

    if (b == 0):
        return 1

    ret = pow(a, b // 2) ** 2 % mod
    if (b % 2 == 0):
        return ret
    else:
        return ret * a % mod


# a부터 b-1까지의 곱을 구함
def fact(a, b):
    global mod
    ret = 1
    for i in range(a, b):
        ret *= i
        ret %= mod
    return ret


if __name__ == '__main__':
    sol11401()