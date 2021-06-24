import sys

input = sys.stdin.readline


# 9375 패션왕 신해빈
# 의상이 종류별로 여러개 주어지고, 종류별 의상은 하나씩만 입을 수 있을때
# 옷을 하나 이상 입는 경우의 수

# 처음엔 어렵게 생각해서 옷 종류를 하나이상 선택하는 모든 조합에
# 각 종류에 해당하는 옷 갯수를 곱하여 더하려고 했지만 시간초과 발생
# 알고보니 옷 종류별 경우의 수, 즉 종류에 해당하는 옷 갯수 + 1(안입은 경우)를 모두 곱한 뒤
# 아무것도 입지않는다는 1개의 경우의 수를 빼는 것이 답이었다.
# 옷의 종류가 k개고 종류별 가짓수가 n1, n2, ... , nk 일 때
# c(n1+1, 1) * c(n2+1, 1) * ... * c(nk+1, 1) - 1
def sol9375():
    answer = []
    for case in range(int(input())):
        ctype = {}
        for _ in range(int(input())):
            n, t = input().split()
            try:
                ctype[t] += 1
            except:
                ctype[t] = 2
        res = 1
        for c in ctype.values():
            res *= c
        answer.append(str(res - 1))

    print('\n'.join(answer))
