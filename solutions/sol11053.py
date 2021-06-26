import sys

input = sys.stdin.read


# 11053 가장 긴 증가하는 부분 수열
# 수열 A의 가장 긴 증가구간의 길이를 찾는 문제
# 흔히 LIS 알고리즘으로 분류되는 문제
# lis 리스트의 마지막 수보다 큰 수가 오면 append, 그렇지 않다면 자신보다 큰 수중 가장 작은 수를 갱신하고
# 모든 수에 처리를 끝낸 뒤 lis 리스트의 길이를 반환하면 해결 가능하다
def sol11053():
    n, *seq = map(int, input().split())
    lis = [seq[0]]
    for num in seq[1:]:
        if num > lis[-1]:
            lis.append(num)
        else:
            for i in range(len(lis)):
                if lis[i] >= num:
                    lis[i] = num
                    break
    print(len(lis))
