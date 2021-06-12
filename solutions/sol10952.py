import sys


# 10952 A+B - 5
def sol10952():
    print('\n'.join(map(str, [sum(map(int, i.split())) for i in sys.stdin.read().splitlines() if i!='0 0'])))
