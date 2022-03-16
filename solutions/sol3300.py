import sys
import re

input = sys.stdin.readline


# 3300 무어 기계
# 대문자 알파벳 심볼과 괄호로 이루어진 패턴에서 하나의 심볼을 _로 치환한 문자열과 출력 문자열이 주어졌을 때
# 출력값이 패턴과 일치하지 않는다면 '!'를 일치하지만 _를 하나의 심볼로 확정지을 수 없다면 '_'를,
# 확정지을 수 있다면 그 심볼을 구하는 문제
def sol3300():
    answer = []

    for _ in range(int(input())):
        symbol = input().rstrip()
        output = input().rstrip()

        # 빈칸을 그대로 둬도 매칭이 된다면 빈칸을 하나로 특정지을 수 없음
        if re.fullmatch(symbol, output):
            answer.append('_')
            continue

        # 빈칸을 알파벳으로 치환하여 어느것과 매치되는지 확인
        wildcard = ord('A')

        # 모든 알파벳에 대해 확인
        for _ in range(26):
            pattern = symbol.replace('_', chr(wildcard))
            # 매칭되는 알파벳 심볼을 찾았다면 break
            if re.fullmatch(pattern, output):
                break
            wildcard += 1

        # 출력값과 매칭되는 알파벳 심볼이 존재했다면 심볼을 answer에 삽입
        answer.append(chr(wildcard) if wildcard <= ord('Z') else '!')

    return '\n'.join(answer)
