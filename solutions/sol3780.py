import sys

input = sys.stdin.readline
mod = 1000


# 3780 네트워크 연결
# n개의 기업이 다음 명령어를 수행한 결과를 구하는 문제
# 1. I A B : A의 센터를 B의 기업과 연결하고 B의 센터를 통합된 클러스터의 센터로 한다
# 2. E A : 기업 A와 A가 속한 클러스터의 센터간의 거리를 출력한다.
# 3. O : 명령입력 종료
# 단, 두 센터 A, B간의 거리는 |A - B| % 1000 이다.
def sol3780():
    answer = []
    for _ in range(int(input())):
        n = int(input())
        u = [[-1, 0] for _ in range(n + 1)]
        while True:
            cmd = input().split()
            # 명령 종료
            if cmd[0] == 'O':
                break

            # 두 클러스터 연결
            if cmd[0] == 'I':
                union(u, int(cmd[1]), int(cmd[2]))

            # 기업과 센터 사이의 거리를 구함
            else:
                answer.append(find(u, int(cmd[1]))[1])

    return '\n'.join(map(str, answer))


def union(u, a, b):
    dist = abs(a - b) % mod
    a, ad = find(u, a)
    b, bd = find(u, b)
    if a != b:
        u[b][0] += u[a][0]
        u[a][0] = b
        u[a][1] = dist + bd


def find(u, x):
    if u[x][0] < 0:
        return [x, 0]
    res = find(u, u[x][0])
    u[x][0] = res[0]
    u[x][1] += res[1]
    return u[x]
