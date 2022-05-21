import sys

input = sys.stdin.readline


# 10840 구간 성분
# 두 문자열의 길이가 같은 구간을 각각 잡아 구간에 속한
# 알파벳의 종류와 갯수가 서로 같은 것을 같은 성분 구간이라 하고
# 알파벳 소문자로 이루어진 문자열 s1, s2가 주어졌을 때
# s1, s2의 같은 성분 구간중 가장 긴 구간의 길이를 구하는 문제
def sol10840():
    s1 = list(map(atoi, input().rstrip()))
    s2 = list(map(atoi, input().rstrip()))

    # s1, s2 사이에 길이가 l인 같은 성분 구간이 존재하는지 확인
    def check(l):
        attrs = set()
        ac = [0] * 26
        for i in range(l):
            ac[s1[i]] += 1
        attrs.add(tuple(ac))
        for i in range(1, len(s1)-l+1):
            ac[s1[i-1]] -= 1
            ac[s1[i+l-1]] += 1
            attrs.add(tuple(ac))

        ac = [0] * 26
        for i in range(l):
            ac[s2[i]] += 1
        if tuple(ac) in attrs:
            return True
        for i in range(1, len(s2)-l+1):
            ac[s2[i-1]] -= 1
            ac[s2[i+l-1]] += 1
            if tuple(ac) in attrs:
                return True
        return False

    # 같은 성분 구간이 존재하는 가장 긴 문자열을 구한다.
    answer = min(len(s1), len(s2))
    while answer >= 0:
        if check(answer):
            break
        answer -= 1

    return answer


def atoi(alpha):
    return ord(alpha) - ord('a')
