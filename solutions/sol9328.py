import sys

input = sys.stdin.readline


# 9328 열쇠
# n * m 크기의 건물안에서 상근이가 규칙에 따라 이동하며 얻을 수 있는 문서의 수를 구하는 문제
# 1. '.' 은 빈 공간을 나타낸다
# 2. '*' 은 벽을 나타낸다
# 3. '$' 는 문서를 나타낸다
# 4. 알파벳 대문자는 문을 나타낸다
# 5. 알파벳 소문자는 열쇠를 나타낸다
# 6. 열쇠는 대응하는 대문자의 문을 열 수 있으며 여러번 사용 가능하다
# 7. 상근이는 상하좌우로 이동 가능하며 건물 가장자리의 빈 공간을 통해 건물 안과 밖을 오갈 수 있다.
# 8. 상근이는 벽을 통과할 수 없다.
def sol9328():
    # 소문자 a의 아스키코드
    ord_key = ord('a')

    # 대문자 A의 아스키코드
    ord_lock = ord('A')

    # 상 하 좌 우 방향벡터
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    answer = []
    for _ in range(int(input())):
        # 건물의 크기
        n, m = map(int, input().split())

        # 건물의 상태
        # 상하좌우 테두리에 빈공간을 두어 상근이가 벽이없는
        # 건물 가장자리를 드나들 수 있도록 함
        board = [['.' for _ in range(m + 2)]]
        for _ in range(n):
            board.append(['.', *input().rstrip(), '.'])
        board.append(['.' for _ in range(m + 2)])

        # 상근이가 보유한 키 현황
        key = [False] * 26

        # 시작부터 보유한 키 체크
        for c in input().rstrip():
            if c == '0':
                break
            key[ord(c) - ord_key] = True

        # (0, 0) 부터 탐색 시작
        doc_count = 0
        q = [(0, 0)]
        board[0][0] = '*'
        locks = []
        while q:
            nq = []
            for r, c in q:
                # 상, 하, 좌, 우로 이동
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < n+2 and 0 <= nc < m+2 and board[nr][nc] != '*':
                        # 문이 있는 칸일 경우 리스트에 추가
                        if board[nr][nc].isupper():
                            locks.append((nr, nc, board[nr][nc]))
                            continue

                        # 문서가 있는 칸일 경우 얻은 문서 수 1 증가
                        if board[nr][nc] == '$':
                            doc_count += 1

                        # 열쇠가 있는 칸일 경우 보유 키 현황 갱신
                        elif board[nr][nc].islower():
                            key[ord(board[nr][nc]) - ord_key] = True

                        # 문서, 열쇠가 있었거나 빈칸이었을 경우 방문처리 후 큐에 삽입
                        board[nr][nc] = '*'
                        nq.append((nr, nc))

            # 탐색중 마주친 문 중에 지금까지 보유한 열쇠로 열 수 있는 문이 있다면 방문처리 후 큐에 삽입
            # 열 수 없다면 다시 잠긴 문 리스트에 삽입
            nlocks = []
            for r, c, t in locks:
                if key[ord(t)-ord_lock]:
                    board[r][c] = '*'
                    nq.append((r, c))
                else:
                    nlocks.append((r, c, t))
            locks = nlocks
            q = nq

        # 얻을 수 있는 문서의 최대 수를 출력
        answer.append(doc_count)
    return '\n'.join(map(str, answer))
