import sys

input = sys.stdin.readline


# 11723 집합
# 집합에서의 삽입, 삭제, 검색, 토글, 채우기, 비우기 연산을 구현하는 문제
# list 나 set 을 사용하여 해결할 수도 있지만 연습을 위해 비트마스크를 사용하여 해결해보았다.
def sol11723():
    # 집합
    s = 0
    for _ in range(int(input())):
        # 명령어
        cmd = input().split()

        # 명령어에 인자가 없을 경우 - all 또는 empty
        if len(cmd) == 1:
            # all 명령어
            # s의 모든 비트값을 1로 초기화
            if cmd[0][0] == 'a':
                s = (1 << 21) - 1

            # empty 명령어
            # s를 0으로 초기화
            else:
                s = 0

        # 명령어에 인자가 존재하는 경우 - add, remove, toggle, check
        else:
            # 인자값의 비트마스크
            e = 1 << int(cmd[1])

            # add 명령어
            # 인자값의 비트마스크와 집합의 비트마스크를 bitwise-or 연산
            if cmd[0][0] == 'a':
                s |= e

            # remove 연산
            # 인자값의 비트마스크에 bitwise-not을 취한 값과 집합의 비트마스크를 bitwise-and 연산
            elif cmd[0][0] == 'r':
                s &= ~e

            # toggle 연산
            # 인자값의 비트마스크와 집합의 비트마스크를 집합의 비트마스크와 bitwise-xor 연산
            elif cmd[0][0] == 't':
                s ^= e

            # 인자값의 비트마스크와 집합의 비트마스크를 bitwise-and 연산한 결과가 0이라면 0
            # 0이 아니라면 1을 출력
            else:
                sys.stdout.write('1\n' if s & e else '0\n')
