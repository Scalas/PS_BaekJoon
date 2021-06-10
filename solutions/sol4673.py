

# 4673 셀프넘버
# 양의 정수 n과 n의 각 자릿수를 더하여 만들 수 없는 수를 구하는 문제
def sol4673():
    d = set()
    i = 1
    while True:
        di = tmp = i
        while tmp > 0:
            di += tmp % 10
            tmp //= 10
        if (di >= 10010):
            break
        d.add(di)
        i += 1

    answer = []
    for i in range(1, 10001):
        if i not in d:
            answer.append(str(i))
    print('\n'.join(answer))
