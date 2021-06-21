import sys

input = sys.stdin.read


# 18870 좌표 압축
# 좌표값들을 입력받아 자신보다 작은 좌표의 갯수를 각각 출력하는 문제
def sol18870():
    n, *nums = map(int, input().split())
    z = {}
    s = sorted(set(nums))
    for i in range(len(s)):
        if not z.get(s[i]):
            z[s[i]] = i
    print(' '.join(map(str, [z[i] for i in nums])))
