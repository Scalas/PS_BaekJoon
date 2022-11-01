import sys

input = sys.stdin.readline


# 2800 괄호 제거
# 올바른 괄호를 포함한 수식이 주어졌을 때
# 올바른 괄호쌍을 하나이상 제거하여 얻을 수 있는 모든 수식을 구하는 문제
def sol2800():
    s = list(input().rstrip())

    # 모든 괄호쌍의 위치를 구함
    par_id = 0
    st = []
    par_pos = []
    for i in range(len(s)):
        c = s[i]
        if c == '(':
            st.append(par_id)
            par_pos.append([i, 0])
            s[i] = ''
            par_id += 1
        elif c == ')':
            par_pos[st.pop()][1] = i

    answer = set()

    # 모든 괄호쌍에 대해 포함 여부를 결정하고 그 결과 얻는 문자열을 answer set에 삽입
    def dfs(cur):
        # 모든 괄호를 처리한 경우
        if cur == par_id:
            answer.add(''.join(s))
            return

        l, r = par_pos[cur]

        # 현재 괄호를 넣고 다음 괄호로
        s[l] = '('
        s[r] = ')'
        dfs(cur + 1)
        s[l] = s[r] = ''

        # 넣지 않고 다음 괄호로
        dfs(cur + 1)

    dfs(0)
    
    # 사전순 정렬한 결과 첫 번째 수식(아무 괄호도 제거하지 않은 수식)을 제외하고 반환
    return '\n'.join(map(str, sorted(answer)[1:]))
