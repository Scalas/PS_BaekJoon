import sys

input = sys.stdin.read


# 17298 오큰수
# 수열에서 각 숫자의 오른쪽에서 숫자보다 크고 가장 왼쪽에 있는 수를 찾는 문제
def sol17298():
    n, *seq = map(int, input().split())
    res = [-1] * n
    st = []
    # 스택에 수열의 수를 순회
    for i in range(n):
        # 자신보다 작은 수는 모두 pop 하고 자신이 그 수의 오큰수가 된다
        while st and st[-1][0] < seq[i]:
            res[st.pop()[1]] = seq[i]

        # 수열에서의 인덱스와 함께 스택에 push
        st.append((seq[i], i))
    return ' '.join(map(str, res))
