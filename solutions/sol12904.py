import sys
import re

input = sys.stdin.readline


# 12904 A와 B
# 문자열 S에 다음 두 연산을 수행하여 문자열 T로 만들 수 있는지 여부를 구하는 문제
# 1. 문자열 뒤에 A를 붙인다.
# 2. 문자열을 뒤집고 뒤에 B를 붙인다.
def sol12904():
    s = input().rstrip()
    t = input().rstrip()

    # A, B의 갯수의 차를 계산
    ac, bc = 0, 0
    for c in t:
        if c == 'A':
            ac += 1
        else:
            bc += 1

    for c in s:
        if c == 'A':
            ac -= 1
        else:
            bc -= 1

    # S에서 문자를 뺄 수는 없기 때문에 T쪽의 문자 수가 적으면 만들 수 없는 문자열
    if ac < 0 or bc < 0:
        return 0

    # B가 나올 때마다 문자열이 뒤집히기 때문에 direction이 1이라면 B는 뒤집힌상태
    direction = bc % 2
    if direction:
        t = t[::-1]

    # T에 마지막으로 문자가 추가된 위치를 알아낸 뒤 규칙에 따라 문자를 한 개씩 벗겨나감
    begin, end = 0, len(t)
    while end - begin > len(s):
        last_added = t[begin] if direction else t[end - 1]

        if direction:
            begin += 1
        else:
            end -= 1

        if last_added == 'B':
            direction = 1 - direction

    # 길이가 같아질 때 까지 문자를 벗겨낸 후 문자열이 동일하다면 S로부터 T를 만들 수 있고
    # 그렇지 않다면 만들 수 없음
    for i in range(len(s)):
        if s[i] != t[i + begin]:
            return 0

    return 1
