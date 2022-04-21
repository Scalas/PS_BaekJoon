import sys

input = sys.stdin.readline
sys.setrecursionlimit(20000)


# 7432 디스크 트리
# 디렉토리의 절대경로명이 n개 주어졌을 때 주어진 경로대로
# 디렉토리를 구성하고 디렉토리의 구조를 출력하는 문제
# 깊이는 공백으로 나타낸다.


# 디렉토리 클래스(노드)
class Directory:
    def __init__(self, name):
        self._name = name
        self._children = []

    def get_name(self):
        return self._name

    def get_children(self):
        return self._children

    def set_name(self, name):
        self._name = name

    def insert_child(self, child):
        self._children.append(child)


def sol7432():
    n = int(input())

    # 루트 디렉토리
    root = Directory('root')

    # 디렉토리 삽입 함수
    def insert_directory(node, path_list):
        # 기존에 존재하는 경로는 타고 들어감
        for child in node.get_children():
            if path_list and child.get_name() == path_list[-1]:
                path_list.pop()
                return insert_directory(child, path_list)

        # 더이상 해당하는 경로가 존재하지 않을 경우
        # 경로대로 디렉토리를 생성
        while path_list:
            node.insert_child(Directory(path_list.pop()))
            node = node.get_children()[-1]

    # 주어진 경로에 따라 디렉토리 삽입
    for _ in range(n):
        path = input().rstrip().split('\\')[::-1]
        insert_directory(root, path)

    # 디렉토리 출력함수
    def dfs(node, depth_exp):
        if node != root:
            print(depth_exp+node.get_name())
            depth_exp += ' '
        children = node.get_children()
        children.sort(key=lambda x: x.get_name())
        for child in children:
            dfs(child, depth_exp)

    dfs(root, '')
