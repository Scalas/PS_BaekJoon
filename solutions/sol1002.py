import sys

input = sys.stdin.read


# 1002 터렛
# 두 원의 교점의 갯수를 구하는 문제
def sol1002():
    answer = []
    for i in input().splitlines()[1:]:
        x1, y1, r1, x2, y2, r2 = map(int, i.split())
        if x1 == x2 and y1 == y2 and r1 == r2:
            answer.append('-1')
            continue

        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
        if r1 > r2:
            maxr, minr = r1, r2
        else:
            maxr, minr = r2, r1

        # 각 원의 중심이 다른 원의 외부에 있을때
        if d > maxr:
            # 한 점에서 만날 때
            if maxr + minr == d:
                answer.append('1')
            # 만나지 않을 때
            elif maxr + minr < d:
                answer.append('0')
            # 두 점에서 만날 때
            else:
                answer.append('2')
        # 한 원의 중심이 다른 원의 내부에 있을 때
        else:
            # 한 점에서 만날 때
            if d + minr == maxr:
                answer.append('1')
            # 두 점에서 만날 때
            elif d + minr > maxr:
                answer.append('2')
            # 만나지 않을 때
            else:
                answer.append('0')
    print('\n'.join(answer))
