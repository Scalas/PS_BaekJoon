import sys

input = sys.stdin.readline


# 2239 스도쿠
# 스도쿠의 빈칸을 채우는 문제
def sol2239():
    sudoku = [[*map(int, list(input().rstrip()))] for _ in range(9)]

    # 행, 열, 3 * 3 정사각형 내의 1~9까지의 숫자 존재여부
    rowset = [[True] * 10 for _ in range(9)]
    colset = [[True] * 10 for _ in range(9)]
    sqset = [[True] * 10 for _ in range(9)]
    sq = [[0] * 9 for _ in range(9)]
    cand = range(1, 10)

    # 빈 칸 탐색 및 각 범위별 숫자의 존재여부 체크
    empty = []
    for i in range(9):
        for j in range(9):
            # 해당 인덱스가 속하는 3 * 3 정사각형 번호
            sq[i][j] = (i // 3) * 3 + (j // 3)
            num = sudoku[i][j]

            # 빈칸이라면 빈칸리스트에 인덱스 추가
            if not num:
                empty.append((i, j))
                continue

            # 빈 칸이 아니라면 해당 행, 열, 3 * 3 정사각형에 해당 숫자가 존재함을 체크
            rowset[i][num] = False
            colset[j][num] = False
            sqset[sq[i][j]][num] = False

    # 빈 칸의 갯수
    empty_count = len(empty)

    def dfs(cur):
        # 빈 칸의 갯수가 채워질 때 까지
        if cur == empty_count:
            return True

        # 빈 칸의 행/열
        r, c = empty[cur]

        # 해당 인덱스의 rowset, colset, sqset
        rs = rowset[r]
        cs = colset[c]
        ss = sqset[sq[r][c]]

        # 모든 범위에 중복숫자가 없는 경우 해당 숫자를 선택하고 다음 빈칸으로
        # 만약 모든 칸을 채우는데 성공한 케이스가 발견되면 바로 return True
        for num in cand:
            if rs[num] and cs[num] and ss[num]:
                sudoku[r][c] = num
                rs[num] = cs[num] = ss[num] = False
                if dfs(cur + 1):
                    return True
                sudoku[r][c] = 0
                rs[num] = cs[num] = ss[num] = True
        return False

    # 빈칸을 하나도 채우지 않은 상태에서 시작
    dfs(0)

    # 완성된 스도쿠 출력
    return '\n'.join([''.join(map(str, sudoku[i])) for i in range(9)])
