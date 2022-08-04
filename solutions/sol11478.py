import sys

input = sys.stdin.readline


# 11478 서로 다른 부분 문자열의 개수
# 문자열 s의 연속하는 부분문자열의 갯수를 구하는 문제
def sol11478():
    string = input().rstrip()
    answer = set()
    for i in range(len(string)):
        substring = ''
        for j in range(i, len(string)):
            substring += string[j]
            answer.add(substring)

    return len(answer)
