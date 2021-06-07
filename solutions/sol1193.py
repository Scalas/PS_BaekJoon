import sys

input = sys.stdin.readline


# 1193 분수찾기
# 분수로 이루어진 수열에서 n번째 수 찾기
# 분모+분자의 합이 같은 분수의 갯수가 1부터 시작해서 1씩 늘어난다는 규칙을 활용하여 쉽게 해결가능
def sol1193():
    x = int(input())
    k = 1
    while True:
        idx = k * (k + 1) // 2 - x
        if (idx >= 0):
            break
        k += 1
    if ((k + 1) % 2 == 0):
        print(f'{idx + 1}/{k - idx}')
    else:
        print(f'{k - idx}/{idx + 1}')
