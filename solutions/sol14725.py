import sys

input = sys.stdin.readline

# 14725 개미굴
# 개미가 가져온 정보를 토대로 개미굴을 그리는 문제
# 트라이 자료구조를 활용하여 해결 가능한 문제이다.


# 트라이의 노드 클래스
# data(키 값), child(자식노드 목록), finished(데이터의 마지막 노드인지 여부)의 세 필드값을 가진다.
class Node:
    # 생성자
    def __init__(self, data=None, finished=False):
        self.data = data
        self.finished = finished
        self.child = {}

    # 노드를 문자열로 표현
    def __str__(self, depth=0):
        res = [str(self.data)]
        for c in self.child.values():
            res.append('--' * depth + c.__str__(depth + 1))
        return '\n'.join(res)


# 트라이 클래스
class Trie:
    # 생성시 빈 노드를 생성하여 루트노드로 설정
    def __init__(self):
        self.root = Node()

    # 삽입 메소드
    def add(self, e):
        # 루트 노드에서 탐색 시작
        cur = self.root

        # 데이터의 각 요소를 키 값으로 하는 노드를 타고내려간다.
        for i in e:
            # 현재 노드의 자식노드 중에
            # 다음 요소를 키 값으로 하는 노드가 존재하지 않는다면 노드를 생성
            # 현재 노드의 자식노드 리스트에 삽입한다.
            if i not in cur.child:
                cur.child[i] = Node(i)
            cur = cur.child[i]
        # 현재 노드가 데이터의 마지막 요소를 키값으로 하는 노드임을 표시
        cur.finished = True

    # 탐색 메소드
    def search(self, key):
        # 루트 노드에서 탐색 시작
        cur = self.root

        # 데이터의 각 요소를 키 값으로 하는 노드를 타고내려간다.
        for c in key:
            # 현재 노드의 자식노드 중에
            # 다음 요소를 키 값으로 하는 노드가 존재하지 않는다면 노드를 생성
            # 찾으려는 데이터가 존재하지 않음을 결과로 반환한다.
            if c in cur.child:
                cur = cur.child[c]
            else:
                return None
        # 탐색이 종료됐을 때, 마지막 노드가 데이터의 마지막 요소를 키 값으로 하는 노드로
        # 표시되어있다면 탐색 성공.  그렇지 않다면 데이터가 존재하지 않음을 결과로 반환한다.
        return cur.data if cur.finished else None

    # 트라이를 문자열로 표현
    def __str__(self):
        return '\n'.join([c.__str__(1) for c in self.root.child.values()])


def sol14725():
    # 로봇개미의 수
    n = int(input())

    # 트라이 인스턴스
    t = Trie()

    # 로봇개미가 가져온 정보를 트라이에 삽입
    for e in sorted([input().split()[1:] for _ in range(n)]):
        t.add(e)

    # 트라이 인스턴스를 문자열화 하여 반환
    return str(t)
