import sys

input = sys.stdin.readline


# 2812 크게 만들기
# 주어진 숫자에서 k개의 자릿수를 지워 만들 수 있는 가장 큰 수를 구하는 문제
def sol2812():
    n, k = map(int, input().split())
    answer = []
    cnt = k
    # 지울 수 있는 횟수가 남아있다면 자신보다 작은 수가 앞자리에 존재하지 않을 때 까지 pop한 뒤 삽입
    for num in list(map(int, input().rstrip())):
        while cnt and answer and answer[-1] < num:
            answer.pop()
            cnt -= 1
        answer.append(num)

    return ''.join(map(str, answer[:n-k]))
