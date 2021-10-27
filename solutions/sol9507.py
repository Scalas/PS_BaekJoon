import sys

input = sys.stdin.read


# 9507 Generations of Tribbles
# 테스트케이스마다 정수 n이 주어지고 아래 규칙을 따르는 변형 피보나치 kfibo의 n 번째 값을 구하는 문제
# kfibo[0] = kfibo[1] = 1
# kfibo[2] = 2
# kfibo[3] = 4
# kfibo[x] = kfibo[x-4] + kfibo[x-3] + kfibo[x-2] + kfibo[x-1]
def sol9507():
    kfibo = [1, 1, 2, 4]
    _, *tc = map(int, input().split())
    for _ in range(4, max(tc)+1):
        kfibo.append(sum(kfibo[-4:]))
    return '\n'.join(map(str, [kfibo[n] for n in tc]))
