import sys

input = sys.stdin.readline


# 2493 탑
# 탑의 높이가 순서대로 주어졌을 때
# 각 탑보다 높이가 높고 왼쪽에있는 탑중 가장 가까운 탑을 구하는 문제
def sol2493():
    n = int(input())
    seq = list(map(int, input().split()))
    answer = [0] * n
    st = []
    for i in range(n - 1, -1, -1):
        num = seq[i]
        while st and st[-1][0] < num:
            answer[st.pop()[1]] = i + 1
        st.append((num, i))
    return ' '.join(map(str, answer))
