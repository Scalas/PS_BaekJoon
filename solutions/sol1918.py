import sys

input = sys.stdin.readline


# 1918 후위 표기식
# 주어진 중위 표기식을 후위 표기식으로 변환하는 문제
def sol1918():
    # 연산자 우선순위
    op = {'+': 0, '-': 0, '*': 1, '/': 1}

    # 중위표기식
    exp = input().rstrip()

    # 피연산자 스택, 연산자 스택
    num_st = []
    op_st = []

    # 괄호의 갯수에 따른 연산자 우선순위 가중치
    priority = 0

    for c in exp:
        # 연산자일 경우
        if c in op:
            # 연산자 우선순위
            op_priority = op[c] + priority

            # 기존에 우선순위가 더 높거나 같은 연산자가 있다면 처리
            while op_st and op_st[-1][1] >= op_priority:
                b = num_st.pop()
                a = num_st.pop()
                o = op_st.pop()[0]
                num_st.append(a + b + o)

            # 스택에 연산자 삽입
            op_st.append((c, op_priority))

        # 여는 괄호일 경우
        elif c == '(':
            priority += 2

        # 닫는 괄호일 경우
        elif c == ')':
            priority -= 2

        # 피연산자일 경우
        else:
            num_st.append(c)

    # 남은 연산자 스택에서 순차적으로 꺼내 처리
    while op_st:
        b = num_st.pop()
        a = num_st.pop()
        o = op_st.pop()[0]
        num_st.append(a + b + o)

    return num_st[0]
