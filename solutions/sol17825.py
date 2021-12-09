import sys

input = sys.stdin.readline


# 17825 주사위 윷놀이
# 칸마다 점수가 적힌 윷놀이판 위에서 네 개의 말을 이동시켜 얻을 수 있는 최대점수를 구하는 문제
def sol17825():
    # 지도의 각 칸별 점수
    map_score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]

    # dfs(cur_map, cur_dice) 의 결과를 저장
    map_state = [dict() for _ in range(10)]

    # 주사위의 눈
    dice = list(map(int, input().split()))

    # src 번째 칸에서 distance 만큼 이동시킬 경우 목적지 번호를 반환
    def move(src, distance):
        if not distance:
            return src

        if src <= 20:
            if src == 5:
                return move(21, distance-1)
            if src == 10:
                return move(24, distance-1)
            if src == 15:
                return move(26, distance-1)

            dst = src + distance
            return dst if dst <= 20 else 32

        if src == 23 or src == 25 or src == 28:
            return move(29, distance-1)

        if src == 31:
            return move(20, distance-1)

        return move(src+1, distance-1)

    # 게임판 상태가 cur_map이고 cur_dice번째 주사위를 굴릴 차례일 때
    # 앞으로 얻을 수 있는 최대점수를 반환
    def dfs(cur_map, cur_dice):
        if cur_dice == 10:
            return 0

        if not map_state[cur_dice].get(cur_map):
            cur_max = 0

            # 4개의 말에 대해
            for i in range(4):
                src = piece_state[i]
                bsrc = 1 << src if src else 0

                # 도착지점에 있는 말은 선택할 수 없음
                if src == 32:
                    continue

                # 해당 말을 이동시킬 경우 목적지
                dst = move(src, dice[cur_dice])
                bdst = 1 << dst

                # 목적지가 도착지점이 아니고 다른 말이 존재할 경우
                # 해당 말은 선택할 수 없음
                if dst < 32 and (cur_map & bdst):
                    continue

                # 선택한 말의 위치를 이동시키보며 백트래킹
                piece_state[i] = dst
                cur_max = max(cur_max, dfs(cur_map - bsrc + bdst, cur_dice+1) + map_score[dst])
                piece_state[i] = src

            # 현재 주사위 순서, 게임판 상태에서 얻을 수 있는 최댓점수 저장
            map_state[cur_dice][cur_map] = cur_max

        # 현재 상태에서 얻을 수 있는 최대점수 반환
        return map_state[cur_dice][cur_map]

    # 말들의 초기 위치
    # 네 말 모두 시작점에 위치
    piece_state = [0, 0, 0, 0]

    # 아무 말도 이동하지 않았고 첫 번째 주사위를 굴릴 차례일 때 최댓점수 반환
    return dfs(0, 0)
