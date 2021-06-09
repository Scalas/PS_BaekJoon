import sys

input = sys.stdin.read


# 1316 그룹 단어 체크
# 같은 문자가 무조건 연속되어 등장하는 그룹단어의 갯수를 세는 문제


# 등장했던 알파벳을 저장해두는 passed 와 이전 알파벳을 나타내는 pre 를 사용하여
# 한번 등장했었고 연속이 끊긴 알파벳이 다시 등장하면 그룹단어가 아닌 것을 알 수 있음
def sol1316():
    print(sum(list(map(check, input().splitlines()[1:]))))


def check(s):
    passed = set()
    pre = None
    res = 1
    for c in s:
        if c == pre:
            continue
        if c in passed:
            res = 0
            break
        passed.add(pre)
        pre = c
    return res
