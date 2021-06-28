import sys


# 17298 오큰수
# 수열에서 각 숫자의 오른쪽에서 숫자보다 크고 가장 왼쪽에 있는 수를 찾는 문제
# 스택에 수열의 수를 순차적으로 push
# 새로 추가된 수는 그보다 작은 수들의 오큰수가 되며 작은 수들은 모두 pop
def sol17298():
    n, *seq = map(int, sys.stdin.read().split())
    answer, st = ['-1'] * n, []
    idx = 0
    for num in seq:
        while st and st[-1][1] < num:
            answer[st.pop()[0]] = str(num)
        st.append((idx, num))
        idx += 1
    print(' '.join(answer))

