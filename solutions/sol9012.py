from sys import stdin


# 9012 괄호
# 괄호의 매칭이 정상적으로 이루어졌는지 확인하는 문제
# 양쪽 괄호의 수가 같아도 매칭은 정상적으로 되지 않을 수 있음
# 스택을 활용해야하는 문제
def sol9012():
    stdin.readline()
    answer = []
    for i in stdin:
        st = []
        res = True
        for c in i.rstrip():
            if c == '(':
                st.append(c)
            elif not st:
                res = False
                break
            else:
                st.pop()

        answer.append('YES' if not st and res else 'NO')
    print('\n'.join(answer))


# 이 문제에서는 열린 괄호가 들어왔을 때 스택에 데이터가 있는지가 관건이기에
# 스택을 단순히 정수형 변수로 하여 +1, -1 로 append, pop 을 대체해도 된다
def sol9012_2():
    stdin.readline()
    answer = []
    for i in stdin:
        st = 0
        for c in i[:-1]:
            if c == '(':
                st += 1
            elif not st:
                st += 1
                break
            else:
                st -= 1

        answer.append('YES' if not st else 'NO')
    print('\n'.join(answer))
