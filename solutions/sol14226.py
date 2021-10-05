import sys

input = sys.stdin.readline


# 14226 이모티콘
# 다음 세 가지 연산을 사용하여 1개의 이모티콘을 s개로 늘리는데 드는 연산의 최소횟수를 구하는 문제
# 1. 화면의 이모티콘을 복사하여 클립보드에 저장
# 2. 클립보드의 이모티콘을 화면에 붙여넣기
# 3. 화면의 이모티콘 하나 삭제
def sol14226():
    # 만들려는 이모티콘의 갯수
    s = int(input())

    # 방문체크 리스트
    # 이미 이모티콘의 수가 s개 이상인 시점부터는 클립보드에 저장할 이유가 없기 때문에
    # 클립보드의 크기는 s를 넘을 수 없으며 자연스럽게 이모티콘의 길이도 2 * s 를 넘지 않는다
    visited = [[False] * (s + 1) for _ in range(2 * s + 1)]

    # BFS 로 각 시간마다 만들어질 수 있는 모든 상태를 체크
    # 초기 상태는 이모티콘이 1개이고 클립보드가 비어있는 상태
    q = [(1, 0)]

    # 해당 상태의 방문여부를 True 로 한다
    visited[1][0] = True

    # 현재시간
    time = 0
    while q:
        nq = []
        for cur, clip in q:
            # 이모티콘 갯수가 s개가 된 경우 현재시간 반환
            if cur == s:
                return time

            # 현재 이모티콘 갯수가 s보다 작고 클립보드의 이모티콘을 붙여넣기한 상태가 아직 방문하지 않은 상태라면
            # 방문상태를 True 로 하고 큐에 삽입
            if cur < s and not visited[cur + clip][clip]:
                visited[cur + clip][clip] = True
                nq.append((cur + clip, clip))

            # 현재 이모티콘 갯수가 1보다 크고 화면의 이모티콘을 하나 지운 상태가 아직 방문하지 않은 상태라면
            # 방문상태를 True 로 하고 큐에 삽입
            if cur > 1 and not visited[cur - 1][clip]:
                visited[cur - 1][clip] = True
                nq.append((cur - 1, clip))

            # 화면의 이모티콘을 클립보드에 저장한 상태가 아직 방문하지 않은 상태라면
            # 방문상태를 True 로 하고 큐에 삽입
            if cur < s and not visited[cur][cur]:
                visited[cur][cur] = True
                nq.append((cur, cur))
        q = nq
        # 시간 1초 증가
        time += 1

    return -1
