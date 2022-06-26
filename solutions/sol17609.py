import sys

input = sys.stdin.readline


# 17609 회문
# 주어진 문자열이 회문이라면 0, 한글자를 지워서 회문이 될 수 있다면 1,
# 둘다 아니라면 2를 출력하는 문제
def sol17609():
    answer = []
    for _ in range(int(input())):
        string = input().rstrip()
        answer.append(check(string, 0, len(string) - 1, 1))
    return '\n'.join(map(str, answer))


def check(s, l, r, cnt):
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1

    if l >= r:
        return 1 - cnt

    if cnt:
        return min(check(s, l + 1, r, cnt - 1), check(s, l, r - 1, cnt - 1))

    else:
        return 2
