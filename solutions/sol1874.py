import sys

input = sys.stdin.readline


# 1874 스택 수열
# 1부터 n 까지의 숫자를 순차적으로 스택에 push 하며 중간에 pop 을 적절히 호출하여 주어진 수열을 만드는 문제
def sol1874():
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    c = 0
    st = []
    answer = []

    # 각 수열의 수들에 대해서
    for num in seq:
        # 그 수가 스택에 추가될 때 까지 push
        while (c < num):
            c += 1
            st.append(c)
            answer.append('+')

        # pop을 했을 때 그 수가 나오지 않는 경우라면 만들 수 없는 수열
        if (not st) or (st[-1] != num):
            answer = False
            break

        # 그 수가 나오는 경우라면 pop
        else:
            st.pop()
            answer.append('-')

    if (answer):
        print(*answer, sep='\n')
    else:
        print('NO')
