import sys

input = sys.stdin.read


# 21964 선린인터넷고등학교 교가
# 입력받은 문자열의 마지막 다섯글자만 출력하는 문제
def sol21964():
    print(input().rstrip()[-5:])
