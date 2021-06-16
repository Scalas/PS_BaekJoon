import sys

input = sys.stdin.read


# 제 5차 천하제일 코딩대회 문제 A
# 입력받은 문자열의 마지막 다섯글자만 출력하는 문제
def solution():
    print(input().rstrip()[-5:])
