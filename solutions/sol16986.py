import sys

input = sys.stdin.readline


# 16986 인싸들의 가위바위보
# 1. 인싸 가위바위보는 n가지의 손동작을 낼 수 있고 손동작간의 승패는 행렬의 형태로 주어진다
# 2. 만약 비긴다면 지우 -> 경희 -> 민호 순으로 순서가 가장 나중인 쪽이 이긴다
# 3. 셋중 누구라도 승수 k에 도달하면 게임이 종료된다
# 지우, 경희, 민호 셋이서 인싸 가위바위보를 할 때
# 지우가 같은 손동작을 두 번 이상 내지 않고 이길 수 있는지 여부를 구하는 문제
def sol16986():
    n, k = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    hands = [list(map(int, input().split())) for _ in range(2)]

    # p1, p2가 각각 s1, s2를 냈을 때 승자를 반환하는 함수
    def judge(p1, p2, s1, s2):
        if table[s1][s2] == 2:
            return p1
        if not table[s1][s2]:
            return p2
        else:
            return max(p1, p2)

    # 지우가 각 손동작을 이미 냈는지 여부
    visited = [False] * n

    # 지우, 경희, 민호의 이긴 횟수와 다음에 내야할 손동작 번호
    # 지우 = -1, 경희 = 0, 민호 = 1
    win = [0] * 3
    idx = [0] * 3

    def dfs(p1, p2):
        # 누군가가 승수 k에 도달했을 때
        if max(win) == k:
            # 도달한 것이 지우라면 1 반환
            if win[-1] == k:
                return 1

            # 그 외의 사람이라면 0 반환
            else:
                return 0

        if p1 > p2:
            p1, p2 = p2, p1

        # 지우가 참여할 경우
        if p1 == -1:
            # 가능한 모든 손동작을 사용해본다
            for i in range(n):
                if visited[i]:
                    continue

                # 손동작을 냈을 때 승자를 구하고 다음 경기를 치를 두 사람을 구함
                winner = judge(p1, p2, i, hands[p2][idx[p2]] - 1)
                np1, np2 = winner, -(p1 + p2)

                # 경희, 민호중 경기를 치른쪽의 다음 손동작 번호를 갱신하고
                # 지우가 낸 손동작을 방문처리, 승자의 승리 횟수를 증가
                idx[p2] += 1
                visited[i] = True
                win[winner] += 1

                # 그상태로 남은 경기를 진행하여 같은 손동작을 내지 않고 이길 수 있는지 확인
                if dfs(np1, np2):
                    return 1

                # 변화된 상태 복구
                win[winner] -= 1
                visited[i] = False
                idx[p2] -= 1

        # 지우가 참여하지 않을 경우 승패는 정해져있음
        else:
            winner = judge(p1, p2, hands[p1][idx[p1]] - 1, hands[p2][idx[p2]] - 1)
            np1, np2 = winner, -(p1 + p2)
            idx[p1] += 1
            idx[p2] += 1
            win[winner] += 1
            if dfs(np1, np2):
                return 1
            win[winner] -= 1
            idx[p2] -= 1
            idx[p1] -= 1

        # 어떤 경우에도 같은 손동작을 내지 않고 이길 수 없었다면 0 반환
        return 0

    return dfs(-1, 0)
