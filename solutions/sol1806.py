import sys

input = sys.stdin.read


# 1806 부분합
# 주어진 수열에서 합이 S 이상인 연속부분수열의 최소길이를 구하는 문제
# 투포인터를 활용하여 간단하게 해결가능
def sol1806():
    n, s, *seq = map(int, input().split())

    if max(seq) >= s:
        return 1
    if sum(seq) < s:
        return 0

    l, r, t = 0, 1, seq[0] + seq[1]
    answer = n
    while True:
        if t < s:
            r += 1
            if r == n:
                break
            t += seq[r]
        else:
            answer = min(answer, r - l + 1)
            t -= seq[l]
            l += 1

    return answer
