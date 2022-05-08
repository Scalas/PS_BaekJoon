import sys

input = sys.stdin.readline


# 5624 좋은 수
# n개의 정수로 이루어진 수열 A가 주어지고
# A[i]가 A[0] ~ A[i-1]의 수를 3번 합하여 만들 수 있으면 A[i]는 좋은 수라고 할 때
# 수열 A의 수 중 좋은 수의 갯수를 구하는 문제
# 같은 위치의 수를 여러번 더할 수도 있다.
def sol5624():
    n = int(input())

    # 수열 A
    seq = list(map(int, input().split()))

    # 좋은 수의 갯수
    answer = 0

    # 이전까지 존재하는 수
    num_set = set()

    # 이전까지 존재하는 수를 두 번 더하여 만들 수 있는 값
    add_set = set()

    for num in seq:
        # 이전까지 존재하는 수에 대하여
        for pre in num_set:
            # num - pre 가 두 수의 합으로 만들 수 있는 값 중에 존재한다면
            # num은 세 수의 합으로 만들 수 있는 수
            if num - pre in add_set:
                answer += 1
                break

        # 만약 num이 새로운 수라면 num_set에 더하고
        # num으로 인해 생긴 두 수의 합을 add_set에 더한다
        if num not in num_set:
            num_set.add(num)
            for pre in num_set:
                add_set.add(pre + num)

    return answer
