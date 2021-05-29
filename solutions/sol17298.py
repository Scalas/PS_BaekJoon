import sys

input = sys.stdin.readline


# 17298 오큰수
# 수열에서 각 숫자의 오른쪽에서 숫자보다 크고 가장 왼쪽에 있는 수를 찾는 문제
# 스택에 수열의 수를 순차적으로 push
# 새로 추가된 수는 그보다 작은 수들의 오큰수가 되며 작은 수들은 모두 pop
def sol17298():
    n = int(input())
    seq = zip(map(int, input().split()), range(n))
    st = []
    answer = [-1] * n
    for num in seq:
        while st and st[-1][0] < num[0]:
            answer[st.pop()[1]] = num[0]
        st.append(num)
    print(' '.join(map(str, answer)))


sol17298()
