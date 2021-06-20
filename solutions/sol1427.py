import sys

input = sys.stdin.readline


# 1427 소트인사이드
# 주어진 수의 자릿수를 정렬하는 문제
# 문자열상태 그대로 리스트화하여 정렬하면 해결가능
def sol1427():
    print(''.join(sorted(list(input().rstrip()), reverse=True)))
