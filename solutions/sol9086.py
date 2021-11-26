import sys

input = sys.stdin.readline


# 9086 문자열
# 각 테스트케이스로 주어진 문자열의 맨앞, 맨뒤 문자열을 이어붙인 문자열을 출력하는 문제
def sol9086():
    answer = []
    for _ in range(int(input())):
        string = input().rstrip()
        answer.append(string[0] + string[-1])
    return '\n'.join(answer)
