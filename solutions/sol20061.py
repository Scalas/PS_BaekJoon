import sys

input = sys.stdin.readline


# 20061 모노미노도미노 2
# 4 x 4 크기의 보드상에 모노미노를 놓으면 아래의 6 x 4 크기의 초록 보드로 떨어지고
# 우측의 4 x 6 크기의 파란 보드의 우측에 붙는 방식으로 블록이 놓아진다.
# 초록 보드의 각 행이 가득차면 그 행이 사라지고 사라진 행만큼의 점수를 얻으며 위쪽 블록들이 그 자리를 채운다
# 파란 보드의 각 열이 가득차면 그 열이 사라지고 사라진 열만큼의 점수를 얻으며 왼쪽 블록들이 그 자리를 채운다
# 초록보드의 0, 1행, 파란보드의 0, 1열에 블록이 있으면 그 블록들이 2행 또는 2열로 내려갈 때 까지
# 아래 또는 오른쪽으로 보드를 민다
# 놓을 모노미노 n개의 형태와 위치가 주어졌을 때 모든 모노미노를 놓은 이후 얻은 점수와 남아있는 블록 수를 구하는 문제
def sol20061():
    n = int(input())
    green = [[0] * 4 for _ in range(6)]
    blue = [[0] * 4 for _ in range(6)]
    score = 0
    for _ in range(n):
        t, r, c = map(int, input().split())
        # 초록 보드로의 이동
        gr, gc = 0, c
        while gr < 6 and not green[gr][gc]:
            if t == 1:
                gr += 1
            elif t == 2 and not green[gr][gc + 1]:
                gr += 1
            elif t == 3 and gr < 5 and not green[gr + 1][gc]:
                gr += 1
            else:
                break
        gr -= 1

        # 블록 놓기
        green[gr][gc] = 1
        if t == 2:
            green[gr][gc + 1] = 1
        elif t == 3:
            green[gr + 1][gc] = 1

        # 초록 보드의 행이 채워졌을 경우
        base, shift = -1, 0
        if t == 3 and sum(green[gr + 1]) == 4:
            base = gr + 1
            shift += 1
        if sum(green[gr]) == 4:
            base = gr
            shift += 1
        if base != -1:
            for i in range(base, base + shift):
                for j in range(4):
                    green[i][j] = 0
            for i in range(base - 1, -1, -1):
                for j in range(4):
                    green[i + shift][j] = green[i][j]
                    green[i][j] = 0
            score += shift

        # 초록 보드의 0, 1 라인에 블록이 존재할 경우
        if gr + shift < 2:
            green = [[0] * 4 for _ in range(2 - (gr + shift))] + green[:gr+shift+4]

        # 파란 보드로의 이동
        br, bc = 0, r
        while br < 6 and not blue[br][bc]:
            if t == 1:
                br += 1
            elif t == 3 and not blue[br][bc + 1]:
                br += 1
            elif t == 2 and br < 5 and not blue[br + 1][bc]:
                br += 1
            else:
                break
        br -= 1

        # 블록 놓기
        blue[br][bc] = 1
        if t == 3:
            blue[br][bc + 1] = 1
        elif t == 2:
            blue[br + 1][bc] = 1

        # 파란 보드의 행이 채워졌을 경우
        base, shift = -1, 0
        if t == 2 and sum(blue[br + 1]) == 4:
            base = br + 1
            shift += 1
        if sum(blue[br]) == 4:
            base = br
            shift += 1
        if base != -1:
            for i in range(base, base + shift):
                for j in range(4):
                    blue[i][j] = 0
            for i in range(base - 1, -1, -1):
                for j in range(4):
                    blue[i + shift][j] = blue[i][j]
                    blue[i][j] = 0
            score += shift

        # 파란 보드의 0, 1 라인에 블록이 존재할 경우
        if br < 2:
            blue = [[0] * 4 for _ in range(2 - (br + shift))] + blue[:br+shift+4]

    return '\n'.join(map(str, [score, sum(map(sum, green)) + sum(map(sum, blue))]))
