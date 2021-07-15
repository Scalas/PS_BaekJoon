import sys

input = sys.stdin.readline


# 3273 두 수의 합
# 주어진 수열에서 합이 특정 값 x가 되는 숫자쌍의 갯수를 구하는 문제


# 방법 1 정렬 후 투포인터 방식으로 해결
# 시작과 끝 포인터를 정렬된 수열의 양쪽 끝에서 시작하여
# 두 수의 합이 x라면 answer += 1, l += 1, r += 1  /  x보다 작다면 l += 1  /  x 보다 크다면 r -= 1
def sol3273():
    n = int(input())
    seq = list(map(int, input().split()))
    x = int(input())
    seq.sort()

    l, r = 0, n - 1
    answer = 0
    while l < r:
        s = seq[l] + seq[r]
        if s == x:
            answer += 1
            l += 1
            r -= 1
        elif s < x:
            l += 1
        else:
            r -= 1
    print(answer)


# 방법 2 주어진 n개의 양의정수는 모두 서로 다르기때문에
# 임의의 수 n에 대해 x-num 또한 수열에 존재한다면 하나의 쌍이 완성된다
# 순서가 바뀌어도 같은 쌍으로 생각해야 하기 떄문에 n < x-n 인 경우만 센다
def sol3273_2():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    answer = 0
    s = set(arr)
    for num in arr:
        if (x - num) in s and num < x - num:
            answer += 1
    print(answer)
