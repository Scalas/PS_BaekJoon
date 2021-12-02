import sys

input = sys.stdin.readline


# 5355 화성 수학
# 특별히 정의된 @, #, % 의 세가지 연산을 사용하여 테스트케이스별 연산결과를 구하는 문제
def sol5355():
    func = {'@': lambda x: x * 3, '%': lambda x: x + 5, '#': lambda x: x - 7}
    answer = []
    for _ in range(int(input())):
        num, *ops = input().split()
        num = float(num)
        for op in ops:
            num = func[op](num)
        answer.append('%.2f' % num)
    return '\n'.join(map(str, answer))
