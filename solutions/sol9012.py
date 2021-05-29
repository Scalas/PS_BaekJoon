import sys

input = sys.stdin.readline


# 9012 괄호
# 괄호의 매칭이 정상적으로 이루어졌는지 확인하는 문제
# 양쪽 괄호의 수가 같아도 매칭은 정상적으로 되지 않을 수 있음
# 스택을 활용해야하는 문제
def sol9012():
    answer = []
    for _ in range(int(input())):
        ps = input().rstrip()
        st = []
        for p in ps:
            if p == '(':
                st.append(p)
            else:
                if st:
                    st.pop()
                else:
                    st.append(p)
                    break
        answer.append('NO') if st else answer.append('YES')
    print(*answer, sep='\n')
