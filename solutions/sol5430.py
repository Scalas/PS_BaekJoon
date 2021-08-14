import sys

input = sys.stdin.readline


# 5430 AC
# 수열을 뒤집는 연산 R, 맨 앞 수를 버리는 연산 D가 있을 때
# 수열과 수열에 적용할 연산리스트를 입력받아 연산을 모두 실행한 결과를 출력하는 문제
# 뒤집을 때마다 D를 입력받았을 때 수를 버릴 위치를 맨 앞과 맨 뒤 사이에서 전환하고
# 입력받은 수열에서 해당 범위만큼을 잘라낸 뒤 뒤집기가 홀수일 경우 뒤집어서 출력하면 해결가능
def sol5430():
    res = []
    for t in range(int(input())):
        cmd = input().rstrip()
        n = int(input())

        # D 연산의 횟수
        d = cmd.count('D')

        seq = input()

        # D 연산의 횟수가 수열의 크기보다 크면 에러
        if d > n:
            res.append('error')
        # 같다면 빈 배열
        elif d == n:
            res.append('[]')

        else:
            seq = list(seq[1:-2].split(','))
            # 두번 연속 뒤집기는 의미가 없음
            cmd = cmd.replace('RR', '')

            # 앞에 나온 R의 횟수가 짝수면 앞에서 버리기, 홀수면 뒤에서 버리기
            cmd = list(map(len, cmd.split('R')))
            seq = seq[sum(cmd[0::2]):n - sum(cmd[1::2])]
            if len(cmd) % 2 == 0:
                seq.reverse()
            res.append('[' + ','.join(seq) + ']')
    return '\n'.join(res)
