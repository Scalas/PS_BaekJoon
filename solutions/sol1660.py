import sys

input = sys.stdin.readline
INF = 10 ** 9


# 1660 캡틴 이다솜
# n개의 대포알을 사면체의 형태로 쌓아두려 할 때
# 쌓아야할 사면체 갯수의 최솟값을 구하는 문제
def sol1660():
    n = int(input())

    # i번째 사면체에 포함된 대포알의 갯수
    tetra = []
    cnt = 1
    i = 1
    while cnt <= n:
        tetra.append(cnt)
        cnt = cnt * (i+3) // i
        i += 1

    # dp안의 값은 사면체의 갯수가 answer 개일 때 만들 수 있는 대포알의 갯수의 합
    dp = {0}
    answer = 0
    while n not in dp:
        answer += 1
        ndp = set()
        escape = False
        for t in tetra:
            for bomb in dp:
                # answer 개의 사면체로 만들 수 있는 대포알의 갯수
                nbomb = t + bomb

                # 대포알의 수가 목표한 갯수(n)보다 작다면 ndp에 삽입
                if nbomb <= n:
                    ndp.add(nbomb)

                # 합이 n이되는 경우를 찾았으면 반복문 종료
                if nbomb == n:
                    escape = True
                    break
            if escape:
                break
        dp = ndp
    return answer
