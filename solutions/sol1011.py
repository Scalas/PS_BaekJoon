import sys
import math

input = sys.stdin.readline


# 1011 Fly me to the Alpha Centauri
# 이동 거리를 1씩만 늘리거나 줄일 수 있는 우주선으로 x부터 y 까지 이동하기위한 최소한의 이동횟수를 구하는 문제
# 단, 최초와 마지막의 이동거리는 1이어야한다
# 이동거리 1로 시작하여 1로끝나면서 이동 횟수를 최소화하려면 1 + 2 + ... + n + .. + 2 + 1 형태를 틀로 잡은 뒤
# 사이사이에 같은거리의 이동을 끼워넣는 방식을 취해야한다
# 예를들어 1에서 10까지라면  1 + 2 + 3 + 2 + 1 이 최소한의 이동횟수로 이동하는 방법이며
# 0에서 10이되면 1 + 1 + 2 + 3 + 2 + 1 또는 1 + 2 + 3 + 2 + 1 + 1 이 될것이다.
# 1 + 2 + ... + n + .. + 2 + 1 의 합은 n^2 이므로
# 이동해야할 거리가 d 라고 할때, d보다 작으면서 가장 큰 n^2의 값을 구한 뒤, 이동횟수에 2*n -1을 더하고
# 남은 거리인 d-n^2 이 0일 경우 그대로 끝, 0보다 크지만 n 이하인 경우 +1
# n보다 큰 경우 n으로 나눈 몫을 이동 횟수에 더한 뒤, 나머지가 0이면 그대로 끝, 0보다 크면 이동횟수에 1을 더한다
def sol1011():
    answer = []
    for t in range(int(input())):
        x, y = map(int, input().split())
        d = y - x
        n = math.floor(math.sqrt(d))
        count = n * 2 - 1

        remain = d - n ** 2
        if remain > n:
            count += remain // n
            remain %= n
        if remain > 0:
            count += 1

        answer.append(str(count))

    print('\n'.join(answer))
