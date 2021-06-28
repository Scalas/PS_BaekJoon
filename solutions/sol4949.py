from sys import stdin


# 4949 균형잡힌 세계
# 괄호 짝맞추기 문제
# 괄호가 아닌 문자가 섞여있고 두종류의 괄호가 등장하는 문제
# 평범한 괄호 문제와 크게 다르지 않다
def sol4949():
    par = {'(', ')', '[', ']'}
    type = {'(': 0, ')': 0, '[': 1, ']': 1}
    side = {'(': 0, '[': 0, ')': 1, ']': 1}
    answer = []
    for i in stdin.read().splitlines()[:-1]:
        st = []
        for c in i:
            if c in par:
                if side[c] == 0:
                    st.append(type[c])
                else:
                    if not st or st[-1] != type[c]:
                        st = [-1]
                        break
                    st.pop()

        answer.append('yes' if not st else 'no')
    print('\n'.join(answer))
