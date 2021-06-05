import sys

input = sys.stdin.readline
dp = {}


# 11729 하노이 탑
# 하노이 탑의 최소이동횟수와 이동과정을 출력하는 문제
# 가장 아래의 원반을 남기고 모든 원반을 현재 원반들이 위치한곳과 최종적으로 이동해야할 위치를 제외한
# 남은 한 위치로 이동시킨 후 맨 아래원반을 최종 목적 위치로 이동시키는 연산을 재귀호출로 반복하면 해결되는 문제
# 처음엔 단순히 재귀만으로 풀었지만 중복으로 계산되는 값이 생각보다 많아 dp를 사용하면 성능을 크게 개선할 수 있었다
def sol11729():
    global answer
    n = int(input())
    res = hanoi(n, 1, 3)
    print(2**n-1, '\n'.join(res), sep='\n')


def hanoi(n, src, dst):
    global dp
    if n == 1:
        return [f'{src} {dst}']
    else:
        res = []
        mdst = 6 - src - dst
        if not dp.get((n - 1, src, mdst)):
            dp[(n - 1, src, mdst)] = hanoi(n - 1, src, mdst)
        res.extend(dp[(n - 1, src, mdst)])
        res.append(f'{src} {dst}')
        if not dp.get((n - 1, mdst, dst)):
            dp[(n - 1, mdst, dst)] = hanoi(n - 1, mdst, dst)
        res.extend(dp[n - 1, mdst, dst])
        return res

