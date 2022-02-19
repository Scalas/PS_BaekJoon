import sys

input = sys.stdin.read


# 17202 핸드폰 번호 궁합
# 010과 -을 제외한 8자리 휴대폰번호 두개가 주어질 때
# 두 번호의 각 자리수를 번갈아가며 나열하고
# 자릿수가 두자리가 될 때까지 인접한 자릿수의 합을 이어붙인 수로 변환하여
# 마지막 두자리를 구하는 문제
# 마지막 두자리의 10의 자리가 0이어도 그대로 출력한다
def sol17202():
    p1, p2 = input().split()
    comp = [*map(int, ''.join([p1[i]+p2[i] for i in range(8)]))]
    for i in range(1, 15):
        comp = [(comp[i]+comp[i+1]) % 10 for i in range(16-i)]
    return ''.join(map(str, comp))
