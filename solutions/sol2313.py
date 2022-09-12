import sys

input = sys.stdin.readline


# 2313 보석 구매하기
# n개의 줄에 각각 m1, m2, ... , mn 개의 보석이 나열되어있고
# 각 줄에서는 연속한 보석만을 구매할 수 있다고 할 때
# 각 줄에서 구매한 보석의 합이 최대가 되도록 하는 경우를 구하는 문제
# 단, 각 줄에서 구매하는 보석의 구간은 같은 가치라면 더 짧은 구간을,
# 같은 길이의 구간이라면 구간을 나타내는 수열이 사전순으로 빠른 것을 구한다.
def sol2313():
    n = int(input())
    max_value = 0
    answers = []
    for _ in range(n):
        m = int(input())
        jewels = list(map(int, input().split()))

        s, e = 0, 0
        max_total = - 10 ** 9
        min_len = 1
        cur_total = 0
        u, v = 0, 0
        while v < len(jewels):
            cur_jewel = jewels[v]
            cur_total += cur_jewel

            if cur_total <= cur_jewel:
                u = v
                cur_total = cur_jewel

            if cur_total > max_total:
                s, e = u, v
                max_total = cur_total
                min_len = v - u + 1
            elif cur_total == max_total:
                if min_len > v - u + 1:
                    s, e = u, v
                    min_len = v - u + 1

            v += 1

        max_value += max_total
        answers.append(' '.join(map(str, [s + 1, e + 1])))

    return str(max_value) + '\n' + '\n'.join(answers)
