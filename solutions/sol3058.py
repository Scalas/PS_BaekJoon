import sys

input = sys.stdin.readline


# 3058 짝수를 찾아라
# 주어진 7개의 수 중 모든 짝수의 합과 짝수중 최솟값을 구하는 문제
def sol3058():
    answer = []
    for _ in range(int(input())):
        evens = [num for num in map(int, input().split()) if not num % 2]
        answer.append(' '.join([str(sum(evens)), str(min(evens))]))

    return '\n'.join(answer)
