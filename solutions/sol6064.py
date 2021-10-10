import sys

input = sys.stdin.readline


# 6064 카잉 달력
# k % m = x,  k % n = y 인 k 를 구하는 문제
def sol6064():
    answer = []
    for t in range(int(input())):
        m, n, x, y = map(int, input().split())

        # m 이 n보다 크도록 한다
        x, y = x if x < m else 0, y if y < n else 0
        if m < n:
            m, n = n, m
            x, y = y, x

        # 마지막 해인 <m, n> 은 m 과 n의 최소공배수 번째 해이다.
        lastyear = lcm(m, n)

        # 만약 x == y == 0이라면 마지막해
        if x == y == 0:
            answer.append(lastyear)
            continue

        # 해당하는 해를 탐색
        find = False
        # k % m 이 x이기 때문에 k는 x부터 시작해서 m 씩 증가하는 값
        # 마지막 해를 넘기면 존재하지 유효하지 않은 표현
        for k in range(x, lastyear + 1, m):
            # 조건에 맞는 해를 찾으면 정답리스트에 추가하고 탐색종료
            if k % n == y:
                answer.append(k)
                find = True
                break
        # 조건에 맞는 해를 찾지 못한 경우 -1을 추가
        if not find:
            answer.append(-1)

    # 출력조건에 맞게 정답리스트 반환
    return '\n'.join(map(str, answer))


# 최소공배수 함수
def lcm(a, b):
    res = a * b
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return res // a
