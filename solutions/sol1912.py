import sys

input = sys.stdin.read


# 1912 연속합
# 입력받은 수열에서 연속된 수를 합했을 때 얻을 수 있는 최댓값을 구하는 문제
# 이전까지 더한 값이 0보다 크다면 더하고 0보다 작다면 자기 자신을 시작으로 다시 더해나간다
def sol1912():
    n, *nums = map(int, input().split())
    dp = answer = -1000
    for num in nums:
        if dp > 0:
            dp += num
        else:
            dp = num
        answer = dp if dp > answer else answer

    print(answer)
