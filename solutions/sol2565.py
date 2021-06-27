import sys

input = sys.stdin.readline


# 2565 전깃줄
# 전깃줄이 교차하지 않게 하기위해 끊어야할 전깃줄 수의 최솟값을 구하는 문제
# 전깃줄을 시작점기준으로 정렬하여 도착점 주소를 기준으로 최장증가수열의 길이를 구하고
# 전체 전깃줄 수에서 최장 증가수열의 길이를 빼주면 구할 수 있다.
def sol2565():
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]
    lines.sort()
    lis = [lines[0][1]]
    for line in lines[1:]:
        num = line[1]
        if num > lis[-1]:
            lis.append(num)
        else:
            for i in range(len(lis)):
                if num < lis[i]:
                    lis[i] = num
                    break
    print(len(lines) - len(lis))
