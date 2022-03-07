import sys

input = sys.stdin.readline


# 3107 IPv6
# 4자리 16진수 8개가 모여서 만들어진 IPv6 주소를 다음과 같은 규칙에 의해 압축할 수 있다
# 1. 앞자리 0 전체 또는 일부를 생략
# 2. 0으로만 이루어진 연속된 그룹이 있을 경우 ::로 치환
# 단, 2번규칙은 한번만 사용가능
# 축약형 IPv6가 주어졌을 때 원래의 32자리 IPv6 주소로 변환하는 문제
def sol3107():
    ipv6 = []
    comp = input().rstrip()
    comp = comp.split('::')
    # 규칙 2가 사용된 경우
    if len(comp) > 1:
        left = [c for c in comp[0].split(':') if c != '']
        right = [c for c in comp[1].split(':') if c != '']

        # :: 기준 좌측의 IPv6 주소 복원
        for c in left:
            ipv6.append('0'*(4-len(c))+c)

        # IPv6 주소의 전체 16진수 갯수인 8에서 좌측, 우측의 16진수의 갯수를 뺀 만큼
        # 0000을 채워넣음
        for _ in range(8-len(left)-len(right)):
            ipv6.append('0000')

        # :: 기준 우측의 IPv6 주소 복원
        for c in right:
            ipv6.append('0'*(4-len(c))+c)

    # 규칙 2가 사용되지 않은 경우
    else:
        for c in comp[0].split(':'):
            ipv6.append('0'*(4-len(c))+c)

    return ':'.join(ipv6)
