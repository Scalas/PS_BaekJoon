import sys

input = sys.stdin.read


# 1264 모음의 개수
# 각 줄의 문장에서 모음의 갯수를 구하는 문제
def sol1264():
    vowel = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    cases = input().splitlines()[:-1]
    return '\n'.join(map(str, [len([c for c in case if c in vowel]) for case in cases]))
