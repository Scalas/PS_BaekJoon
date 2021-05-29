import sys

input = sys.stdin.readline
answer = []
param = 0


def push(st):
    global param
    st.append(param)


def pop(st):
    answer.append(-1 if not st else st.pop())


def size(st):
    answer.append(len(st))


def empty(st):
    answer.append(0 if st else 1)


def top(st):
    answer.append(-1 if not st else st[-1])


# 10828 스택
# 간단한 스택을 구현하는 문제
# dictionary 로 명령어에 해당하는 함수를 매칭하여 구현
def sol10828():
    n = int(input())
    global param
    st = []
    func = {'push': push, 'pop': pop, 'size': size, 'empty': empty, 'top': top}
    for _ in range(n):
        cmd = input().split()
        if (len(cmd) == 2):
            param = int(cmd[1])
        func[cmd[0]](st)
    print(*answer, sep='\n')
