import sys

input = sys.stdin.readline


# 25178 두라무리 휴지
# 길이 n의 문자열 두 개가 주어졌을 때
# 1. 두 문자열의 문자 위치를 재배열하면 서로 같아질 수 있음
# 2. 두 문자열의 양 끝 문자는 서로 같음
# 3. 두 문자열에서 모음을 제거하면 서로 같음
# 위 세 가지 조건을 만족하는지 여부를 구하는 문제
def sol25178():
    n = int(input())
    w1 = input().rstrip()
    w2 = input().rstrip()

    # 재배열하여 같아질 수 없다면 NO
    alpha = [0] * 26
    vowel = {'a', 'e', 'i', 'o', 'u'}
    for i in range(n):
        alpha[ord(w1[i]) - ord('a')] += 1
        alpha[ord(w2[i]) - ord('a')] -= 1

    for count in alpha:
        if count:
            return 'NO'

    # 양 끝 문자가 다르다면 NO
    if w1[0] != w2[0] or w1[-1] != w2[-1]:
        return 'NO'

    # 모음을 제거했을 때 다르다면 NO
    w1_cons = [c for c in w1 if c not in vowel]
    w2_cons = [c for c in w2 if c not in vowel]
    if w1_cons != w2_cons:
        return 'NO'

    return 'YES'
