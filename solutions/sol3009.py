import sys

input = sys.stdin.read


# 3009 네 번째 점
# 직사각형의 세 점이 주어졌을때 나머지 한 점을 구하는 문제
def sol3009():
    x, y = set(), set()
    for i in input().splitlines():
        xp, yp = map(int, i.split())
        if xp in x:
            x.remove(xp)
        else:
            x.add(xp)
        if yp in y:
            y.remove(yp)
        else:
            y.add(yp)
    print(*(list(x)+list(y)))


if __name__ == '__main__':
    sol3009()
