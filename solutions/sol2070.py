import sys

input = sys.stdin.readline


# 2070 목걸이 수열
# 1과 0으로 이루어진 수열이 주어졌을 때 세 가지 조건을 만족하도록 수열을 쪼갠 결과를 구하는 문제
# 조건
# 1. 쪼개진 각 수열은 목걸이 수열이다
# 2. 인접한 두 수열을 합쳤을 때 목걸이 수열이 되지 않는다.
# 3. 쪼개진 수열들은 크기가 감소한다.
# 목걸이 수열이란 수열을 회전시켜 만들 수 있는 모든 숫자중 가장 작은 값을 가지는 수열을 말함
# 수열의 크기비교는 사전방식으로 이루어짐
def sol2070():
    seq = input().rstrip()
    n = len(seq)

    answer = []
    tmp = []
    pre = '0'
    # 수열 파싱
    for c in seq:
        if c == '1':
            tmp.append(c)
        else:
            # [0...1...] 형태가 완성된 경우
            if pre == '1':
                # 완성된 조각을 answer 스택에 삽입
                new_frag = ''.join(tmp)
                answer.append(new_frag)

                # 만약 스택의 맨 위 두 조각을 합쳐 목걸이 수열을 만들 수 있거나
                # 스택 맨 위의 조각이 맨 위에서 두 번째 조각보다 클 경우
                # 맨 위의 두 조각을 병합
                while len(answer) > 1:
                    if compare(answer[-2], answer[-1]) or is_neck(answer[-2], answer[-1]):
                        o2 = answer.pop()
                        o1 = answer.pop()
                        answer.append(o1 + o2)
                    else:
                        break
                tmp, pre = [c], '0'
            else:
                tmp.append(c)
        pre = c

    # 마지막 조각에 대한 처리
    new_frag = ''.join(tmp)
    answer.append(new_frag)
    while len(answer) > 1:
        if compare(answer[-2], answer[-1]) or is_neck(answer[-2], answer[-1]):
            o2 = answer.pop()
            o1 = answer.pop()
            answer.append(o1 + o2)
        else:
            break

    # 병합되지 않고 남아있는 조각들을 각각 괄호로 감싼 뒤 이어붙여 반환
    return '(' + ')('.join(answer) + ')'


# 두 수열의 비교함수
def compare(o1, o2):
    for i in range(min(len(o1), len(o2))):
        if o1[i] > o2[i]:
            return False
        if o1[i] < o2[i]:
            return True

    return len(o1) <= len(o2)


# 두 수열을 합쳐 목걸이 수열이 되는지 확인
def is_neck(o1, o2):
    if o1 + o2 <= o2 + o1:
        return True
    else:
        return False
