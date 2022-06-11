import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


# 14238 출근 기록
# A는 매일 출근 가능하고 B는 출근한 다음날을 쉬어야하며 C는 출근한 다음날과 다다음날을 쉬어야하고
# 위 조건을 만족하는 출근기록을 올바른 출근기록이라고 한다.
# A, B, C로만 이루어진 최대길이 50의 출근기록이 주어졌을 때
# 주어진 출근기록의 순열중 올바른 출근기록중 하나를 출력하는 문제
# 만약 올바른 출근기록이 존재하지 않을경우 -1을 출력한다.
def sol14238():
    record = input().rstrip()
    n = len(record)

    # 주어진 출근기록에 포함된 A, B, C의 출근횟수를 카운팅
    count = [0, 0, 0]
    for c in record:
        if c == 'A':
            count[0] += 1
        elif c == 'B':
            count[1] += 1
        else:
            count[2] += 1

    # visited[i][a][b][c][s] 는 i일째 출근할사람을 선택할 차례이고
    # 전날까지의 a, b, c의 출근횟수가 각각 a, b, c이며
    # 최대 2일전까지 출근한 사람에 따른 상태가 s인 상황을 이미 탐색했는지 여부
    visited = [[[[[False] * 5 for _ in range(count[2]+1)] for _ in range(count[1]+1)] for _ in range(count[0]+1)] for _ in range(n)]

    # answer의 초기값은 -1
    answer = '-1'

    # 백트래킹을 위한 스택
    st = []

    # 탐색 성공여부를 나타내기 위한 플래그
    finished = False

    # b가 출근할 수 있는 상태, c가 출근할 수 있는 상태
    b_set = {0, 2, 4}
    c_set = {0, 1}

    # 출근가능여부 계산
    def state(st):
        # 이전에 출근한사람이 없을 경우 모든 사람이 출근가능
        if not st:
            return 0

        # 이전에 출근한 사람이 C인 경우
        if st[-1] == 'C':
            return 4

        # 이전에 출근한 사람이 A인 경우
        if st[-1] == 'A':
            # 이전에 출근한 사람이 하나뿐이거나 C가 아닐 경우
            if len(st) == 1 or st[-2] != 'C':
                return 0
            return 2

        # 이전에 출근한 사람이 B인 경우
        if st[-1] == 'B':
            # 이전에 출근한 사람이 하나뿐이거나 C가 아닐 경우
            if len(st) == 1 or st[-2] != 'C':
                return 1
            return 3

    # dfs로 각 일수마다 누가 출근할지를 결정
    def dfs(idx, a, b, c, s):
        nonlocal answer, finished

        # 올바른 출근기록을 완성했을 경우
        # answer를 올바른 출근기록으로 갱신후 탐색종료
        if idx == n:
            answer = ''.join(st)
            finished = True
            return

        # 이미 방문한 케이스인 경우
        if visited[idx][a][b][c][s]:
            return

        # 방문처리
        visited[idx][a][b][c][s] = True

        # A를 출근시킬 경우
        if a < count[0]:
            st.append('A')
            dfs(idx + 1, a + 1, b, c, state(st))
            if finished:
                return
            st.pop()

        # B를 출근시킬 경우
        if s in b_set and b < count[1]:
            st.append('B')
            dfs(idx + 1, a, b + 1, c, state(st))
            if finished:
                return
            st.pop()

        # C를 출근시킬 경우
        if s in c_set and c < count[2]:
            st.append('C')
            dfs(idx + 1, a, b, c + 1, state(st))
            if finished:
                return
            st.pop()

    dfs(0, 0, 0, 0, 0)

    return answer
