import sys

input = sys.stdin.read


# 1874 스택 수열
# 1부터 n 까지의 숫자를 순차적으로 스택에 push 하며 중간에 pop 을 적절히 호출하여 주어진 수열을 만드는 문제
def sol1874():
    n, *nums = map(int, input().split())
    cur = 1
    st = []
    answer = []
    for num in nums:
        while cur <= num:
            st.append(cur)
            answer.append('+')
            cur += 1
        if st[-1] != num:
            answer = ['NO']
            break
        st.pop()
        answer.append('-')
    print('\n'.join(answer))
