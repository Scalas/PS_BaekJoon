import sys

input = sys.stdin.readline

# 14425 문자열 집합
# 트라이 자료구조의 연습문제.
# 물론 해시 등을 사용하여 더 쉽게 해결 가능하지만 연습을 위해 트라이를 사용하여 해결하였다.


# 트라이의 노드 클래스
# data(키 값), child(자식노드 목록), finished(데이터의 마지막 노드인지 여부)의 세 필드값을 가진다.
class Node:
    def __init__(self, data=None, finished=False):
        self.data = data
        self.finished = finished
        self.child = {}


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


def sol14425():
    # 집합에 속한 문자열의 갯수 N, 검사할 문자열의 갯수 M
    n, m = map(int, input().split())

    # 입력된 모든 문자열
    strings = sys.stdin.read().split()

    # N개의 문자열을 트라이에 삽입
    t = Trie()
    for i in range(n):
        t.add(strings[i])

    # M개의 문자열을 모두 탐색하여 몇 개의 문자열이 트라이에 존재하는지 센다
    cnt = 0
    for i in range(n, n + m):
        cnt += (1 if t.search(strings[i]) else 0)

    # 결과반환
    return cnt
