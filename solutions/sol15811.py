import sys

input = sys.stdin.readline


# 15811 복면산?!
# 0-9까지의 수를 임의의 대문자 알파벳으로 치환한 문자열 u, v, w가 순서대로 주어졌을 때
# u + v = w가 성립하는 치환 방식이 존재한다면 YES, 존재하지 않는다면 NO를 반환하는 문제
# 각 숫자는 서로 다른 알파벳으로만 치환 가능하며 숫자는 0으로 시작할 수 있다.
def sol15811():
    u, v, w = input().rstrip().split()
    # 각 문자열들의 맨 뒷자리 문자부터 매핑 딕셔너리에 삽입
    # 초기값은 -20
    d = {}
    for i in range(max(len(u), len(v), len(w))):
        if len(u) > i and u[-1-i] not in d:
            d[u[-1-i]] = -20
        if len(v) > i and v[-1-i] not in d:
            d[v[-1-i]] = -20
        if len(w) > i and w[-1-i] not in d:
            d[w[-1-i]] = -20

    # 알파벳 리스트
    alpha = list(d.keys())

    # 0-9 까지의 숫자 사용여부 체크
    used = [False] * 10

    # 체크 길이
    check_len = min(len(u), len(v), len(w))

    # dfs(i) 는 alpha의 i번째 문자를 치환하는 단계
    def dfs(cur):
        # 만약 마지막 문자까지 치환이 완료되었다면
        # 수식이 성립하는지 체크
        if cur == len(alpha):
            ui = int(''.join(map(lambda x: str(d[x]), u)))
            vi = int(''.join(map(lambda x: str(d[x]), v)))
            wi = int(''.join(map(lambda x: str(d[x]), w)))
            if ui + vi == wi:
                return True
            return False

        for i in range(10):
            # 문자 하나를 아직 사용되지 않은 숫자로 치환
            if not used[i]:
                d[alpha[cur]] = i

                # 모순이 없는지 체크
                # 올림수
                up = [0] * (check_len+1)
                check = False
                # 각 수의 맨 끝자리부터 u와 v를 더한 값을 10으로 나눈 나머지가 w가 되는지 확인
                for j in range(check_len):
                    x, y, z = d[u[-1-j]], d[v[-1-j]], d[w[-1-j]]
                    # x, y, z의 초기값은 -20이므로 셋 중 하나라도 값을 아직 찾지 않았다면 음수
                    if x+y+z > 0:
                        # 세 자릿수 모두 정해진 상태로 수식이 성립하지 않는다면 더이상 탐색할 필요 없음
                        if not ((x + y + up[j]) % 10 == z):
                            check = True
                            break
                        # 올림수 처리
                        up[j+1] = (x + y + up[j]) // 10
                    # 세 자릿수가 모두 정해지지 않았다면 더이상 체크 불가
                    else:
                        break

                # 만약 더이상 탐색할 필요가 없다면 이전 단계로 돌아감
                if check:
                    d[alpha[cur]] = -20
                    continue

                # 더 탐색해볼 필요가 있다면 치환한 숫자를 사용처리하고 다음단계로
                used[i] = True

                # 만약 하나라도 성공케이스가 존재한다면 성공
                if dfs(cur+1):
                    return True

                # 원 상태로 복귀
                d[alpha[cur]] = -20
                used[i] = False

        # 성공케이스를 하나도 찾지 못했다면 실패
        return False

    # 성립 가능한 수식의 존재여부 반환
    return 'YES' if dfs(0) else 'NO'
