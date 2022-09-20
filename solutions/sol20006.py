import sys

input = sys.stdin.readline


# 20006 랭킹전 대기열
# p 명의 플레이어는 각각 레벨과 닉네임을 가지고있고 방의 정원은 m이며
# 방의 레벨은 방을 생성한 플레이어의 레벨과 같다.
# 플레이어는 자신의 레벨의 -10 에서 +10 까지의 방에 들어갈 수 있고
# 그러한 방이 존재한다면 그 중 가장 먼저 생성된 방에 들어간다.
# 방이 없다면 새로 방을 만든다.
# 방의 정원은 m이며 정원이 차면 더이상 들어갈 수 없고 게임이 시작된다.
# 모든 플레이어의 입장이 끝난 후 방의 게임 시작여부, 방에 들어간 플레이어들의 레벨과 닉네임을
# 방의 생성 순서대로 출력한다. 단, 플레이어들의 레벨과 닉네임은 닉네임 사전순으로 정렬하여 출력한다.
def sol20006():
    p, m = map(int, input().split())
    
    # 방과 각 방의 레벨
    rooms = []
    levels = []
    for _ in range(p):
        lv, nickname = input().split()
        lv = int(lv)
        
        # 입장 시도
        entered = False
        for room_idx in range(len(rooms)):
            if not (lv - 10 <= levels[room_idx] <= lv + 10):
                continue

            room = rooms[room_idx]
            if len(room) == m:
                continue

            room.append((nickname, lv))
            entered = True
            break
        
        # 입장 실패시 방 생성
        if not entered:
            room = [(nickname, lv)]
            rooms.append(room)
            levels.append(lv)
    
    # 방의 게임 시작 여부와 유저 정보 출력
    answer = []
    for room_idx in range(len(rooms)):
        room = rooms[room_idx]
        room.sort()
        answer.append('Started!' if len(room) == m else 'Waiting!')
        for player in room:
            answer.append(' '.join(map(str, player[::-1])))

    return '\n'.join(answer)
