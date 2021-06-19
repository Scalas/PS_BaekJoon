from sys import stdin


# 7568 덩치
# 키가 몸무게가 모두 큰 사람의 수+1을 각각 구하는 문제
def sol7568():
    stdin.readline()
    size = [tuple(map(int, i.split())) for i in stdin]
    l = len(size)
    answer = [1] * l
    for i in range(l):
        for j in range(i + 1, l):
            xd, yd = size[i][0] - size[j][0], size[i][1] - size[j][1]
            if xd * yd > 0:
                if xd > 0:
                    answer[j] += 1
                else:
                    answer[i] += 1
    print(' '.join(map(str, answer)))
