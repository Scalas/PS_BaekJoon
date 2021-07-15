import sys

input = sys.stdin.read


# 2470 두 용액
# 서로 다른 특성값을 가진 용액들이 주어졌을때 두 용액의 합이 0에 가장 가까운 경우를 찾는 문제

# 전형적인 투 포인터 문제
# 용액을 특성순으로 오름차순 정렬한 뒤 합이 가장 0에 가까운 두 용액의 값을 갱신시키며
# 합이 음수라면 l += 1,  양수라면 r -= 1 로 탐색해나간다
def sol2470():
    n, *liq = map(int, input().split())
    liq.sort()
    if liq[0] >= 0:
        return ' '.join(map(str, [liq[0], liq[1]]))
    if liq[-1] <= 0:
        return ' '.join(map(str, [liq[-2], liq[-1]]))

    l, r = 0, n - 1
    x, y, res = 0, 0, float('inf')
    while l < r:
        s = liq[l] + liq[r]
        if s == 0:
            x, y = l, r
            break
        if s < 0:
            if -s < res:
                x, y, res = l, r, -s
            l += 1
        else:
            if s < res:
                x, y, res = l, r, s
            r -= 1

    return ' '.join(map(str, [liq[x], liq[y]]))
