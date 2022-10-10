import sys

input = sys.stdin.readline


# 1725 히스토그램
# n개의 막대로 이루어진 히스토그램이 주어졌을 때
# 그 안에서 만들어질 수 있는 가장 큰 직사각형의 크기를 구하는 문제
# 분할정복이나 세그먼트 트리 등을 사용할 수도 있지만 스택으로 간단하게 해결할 수도 있다
def sol1725():
    n = int(input())

    # 히스토그램 스택 안의 막대는 모두 오름차순이기 때문에 마지막에 pop한 막대의 높이 * 지금까지 pop한 갯수가
    # 현재 막대를 온전히 포함할 경우 가장 넓은 직사각형이 된다.
    # 막대 하나가 들어올 때 마다 이전의 막대중 자신보다 큰 막대들을 pop 하면서
    # pop한 막대 * 지금까지 pop한 막대 갯수 로 answer 을 갱신한다.
    # 그리고 새로 들어오는 막대는 pop한 막대의 수 + 1 만큼의 갯수를 가지게된다.
    hist = []
    answer = 0
    for _ in range(n):
        cur = int(input())
        count = 0
        while hist and hist[-1][0] > cur:
            pre, cnt = hist.pop()
            count += cnt
            answer = max(answer, count * pre)
        if hist and hist[-1][0] == cur:
            hist[-1][1] += (count + 1)
        else:
            hist.append([cur, count + 1])

    # 마지막으로 스택에 남아있는 모든 막대를 pop 하면서 answer 를 갱신한다.
    count = 0
    while hist:
        pre, cnt = hist.pop()
        count += cnt
        answer = max(answer, count * pre)

    return answer
