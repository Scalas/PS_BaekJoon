import sys

input = sys.stdin.readline


# 9093 단어 뒤집기
# 주어진 문자열들을 단어들을 뒤집은 상태로 출력하는 문제
# ex) "I am a student"  =>  "I ma a tneduts"
def sol9093():
    res = []
    for _ in range(int(input())):
        res.append(' '.join(([s[::-1] for s in input().split()])))
    return '\n'.join(res)
