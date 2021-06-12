import sys


# 10951 A+B - 4
def sol10951():
    print('\n'.join(map(str, [sum(map(int, i.split())) for i in sys.stdin.read().splitlines()])))
