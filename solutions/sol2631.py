import sys
from bisect import bisect_left

input = sys.stdin.read


# 2631 줄세우기
# 학생들의 번호가 현재 줄선 순서대로 주어졌을 때
# 오름차순으로 정렬시키기 위해 자리를 옮겨야할 학생의 수를 구하는 문제

# 이미 오름차순으로 서있는 학생들은 그대로 두고 순서에 맞지않는 학생들만 위치를 옮기면 되기 때문에
# 주어진 수열의 최장 증가 부분 수열의 길이를 구한 뒤 학생의 수에서 빼주면 된다.
def sol2631():
    # 학생의 수, 번호 수열
    n, *nums = map(int, input().split())

    # LIS 알고리즘을 수행하여 번호 수열의 최장 증가 부분 수열의 길이를 구한다
    lis = [0]
    for num in nums:
        if num > lis[-1]:
            lis.append(num)
        else:
            lis[bisect_left(lis, num)] = num

    # (학생의 수 - 최장 증가 부분 수열의 길이) 반환
    return n - len(lis) + 1
