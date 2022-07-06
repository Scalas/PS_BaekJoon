import sys
from math import log2, floor

sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 1493 박스 채우기
# length * width * height 크기의 직육면체를 주어진 모서리 길이가 2 ^ n인 큐브들로 채울 때
# 필요한 큐브의 수의 최솟값을 구하는 문제
def sol1493():
    length, width, height = map(int, input().split())
    n = int(input())

    # 크기별 큐브의 수
    cubes = [0] * 21
    for _ in range(n):
        u, v = map(int, input().split())
        cubes[u] = v

    # 크기별 큐브의 모서리 길이
    cube_len = [1]
    for _ in range(20):
        cube_len.append(cube_len[-1] * 2)

    # 크기별 큐브의 부피
    cube_size = [cube_len[i] ** 3 for i in range(21)]

    # 크기별 큐브의 필요량
    cube_need = [0] * 21

    # 직육면체를 채우기 위해 필요한 크기별 큐브의 갯수를 구함
    def dnc(l, w, h):
        if not l * w * h:
            return 0

        # 채울 수 있는 가장 큰 큐브의 종류
        max_cube = floor(log2(min(l, w, h)))
        cl = cube_len[max_cube]

        # 각 방향으로 가장 큰 큐브가 들어가는 갯수
        lc = l // cl
        wc = w // cl
        hc = h // cl

        cube_need[max_cube] += lc * wc * hc
        cl = cube_len[max_cube]
        nl, nw, nh = cl * lc, cl * wc, cl * hc
        dnc(nl, nw, h - nh)
        dnc(nl, w - nw, nh)
        dnc(nl, w - nw, h - nh)
        dnc(l - nl, w, h)

    dnc(length, width, height)

    # 필요한 큐브를 주어진 큐브로 만들기 위해 필요한 실제 큐브의 갯수를 구함
    res = 0
    for c in range(20, -1, -1):
        if not cube_need[c]:
            continue

        tmp = cube_size[c] * cube_need[c]
        for i in range(c, -1, -1):
            # 큐브가 남아있지 않다면 continue
            if not cubes[i]:
                continue

            # i 큐브의 크기
            size = cube_size[i]

            # max_cube를 채우기 위해 사용할 i큐브의 갯수
            cnt = min(tmp // size, cubes[i])

            # 사용한 큐브만큼 tmp 감소, cubes[i] 감소, res 증가
            cubes[i] -= cnt
            tmp -= size * cnt
            res += cnt

            # max_cube 완성시 break
            if not tmp:
                break
        if tmp:
            return -1

    return res
