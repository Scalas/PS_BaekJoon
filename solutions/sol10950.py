import sys


# 10950 A+B - 3
def sol10950():
    print('\n'.join(map(str, [sum(map(int, i.split())) for i in sys.stdin.read().splitlines()[1:]])))
