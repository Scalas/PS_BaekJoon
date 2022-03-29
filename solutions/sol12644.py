import sys

input = sys.stdin.readline


# 12644 Decision Tree(Large)
# 괄호, 알파벳, 가중치(소수)로 구성된 의사결정트리를 파싱하여 확률값을 구하는 문제
def sol12644():
    answers = []
    for i in range(1, int(input())+1):
        answer = ['Case #%d:' % i]

        # 의사결정 트리 파싱
        dt_string = ''.join([input().strip() for _ in range(int(input()))])
        root = dfs(0, dt_string)

        # 동물 평가
        for _ in range(int(input())):
            # 동물의 이름과 속성
            name, _, *attr = input().split()
            attr = set(attr)

            # 노드 idx(루트)
            cur = root

            # 동물이 귀여울 확률 초기값(루트값)
            p = cur.get_weight()

            # 자식노드가 있는 경우
            while not cur.is_leaf():
                # 다음 노드(초기값 우측노드)
                nxt = cur.get_left() if cur.get_keyword() in attr else cur.get_right()

                # 다음 노드의 가중치를 곱하고 이동
                p *= nxt.get_weight()
                cur = nxt

            answer.append('%.7f' % p)
        answers.append('\n'.join(answer))

    return '\n'.join(answers)


def dfs(idx, dts):
    # 양 끝 괄호 제거
    dts = dts.strip()[1:-1]
    sub_start = dts.find('(')

    # 리프노드인 경우
    if sub_start < 0:
        return Node(float(dts), '')

    # 리프노드가 아닌 경우
    else:
        u, v = dts[:sub_start].strip().split()
        u = float(u)
        cur = Node(u, v)

        # 첫째 열린 괄호부터 파싱 시작
        ci = sub_start

        # 왼쪽 자식노드
        st = [dts[ci]]
        ci += 1
        while st:
            if dts[ci] == '(':
                st.append('(')
            elif dts[ci] == ')':
                st.pop()
            ci += 1
        cur.set_left(dfs(idx * 2 + 1, dts[sub_start:ci]))

        # 우측 자식노드
        cur.set_right(dfs(idx * 2 + 2, dts[ci:]))

        return cur


class Node:
    def __init__(self, weight, keyword):
        self.__weight = weight
        self.__keyword = keyword
        self.__left = None
        self.__right = None

    def set_left(self, left_node):
        self.__left = left_node

    def set_right(self, right_node):
        self.__right = right_node

    def get_weight(self):
        return self.__weight

    def get_keyword(self):
        return self.__keyword

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def is_leaf(self):
        return self.__keyword == ''
