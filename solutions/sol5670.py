import sys

input = sys.stdin.readline

# 5670 휴대폰 자판
# 자동완성 기능을 가진 휴대폰 자판으로 단어들을 타이핑할 때
# 필요한 타이핑 횟수의 평균값을 구하는 문제.
# 트라이 자료구조를 활용하여 해결 가능한 문제이다.


# 트라이의 노드 클래스
# data(키 값), child(자식노드 목록), finished(데이터의 마지막 노드인지 여부), cnt(거쳐간 단어의 수)의 네 개의 필드값을 가진다.
class Node:
    def __init__(self, data=None, finished=False):
        self.data = data
        self.finished = finished
        self.child = {}
        self.cnt = 0


# 트라이 클래스
class Trie:
    # 생성시 빈 노드를 생성하여 루트노드로 설정
    def __init__(self):
        self.root = Node(finished=True)

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

            # 해당 노드를 거쳐간 문자열의 수를 1 증가시킨다.
            cur.child[i].cnt += 1

            cur = cur.child[i]
        # 현재 노드가 데이터의 마지막 노드임을 표시
        cur.finished = True

    # 트라이의 루트노드를 반환
    def get_root(self):
        return self.root


def sol5670():
    # 케이스의 정답 목록을 저장할 리스트
    answer = []

    for n in sys.stdin:
        # 케이스별 영단어의 갯수
        n = int(n)

        # 단어 리스트
        words = [input().strip() for _ in range(n)]

        # 트라이에 모든 단어를 삽입
        t = Trie()
        for word in words:
            t.add(word)

        # 루트노드의 모든 자식노드들에 대해 dfs 를 실행, 그 결과를 모두 더한다
        # res 값은 모든 영단어를 타이핑하기 위해 버튼을 눌러야할 횟수의 총합
        res = 0
        root = t.get_root()
        for cur in root.child.values():
            res += dfs(root, cur)

        # 평균값을 소숫점 셋째자리에서 반올림하여 answer 리스트에 삽입
        answer.append('%.2f' % (res / n))

    # 출력형식에 맞춰 정답리스트 반환
    return '\n'.join(answer)


# 탐색 함수
def dfs(parent, node):
    # 버튼을 눌러야 할 횟수
    res = 0

    # 현재 노드가 부모노드의 유일한 자식노드이거나
    # 부모노드가 데이터의 마지막 노드로 표시되어있을 경우
    # 자동완성이 되지 않기 때문에 버튼을 눌러야함
    if parent.finished or len(parent.child) > 1:
        res += node.cnt

    # 자식노드에 대해 탐색함수 재귀호출하여 결과값을 res 에 가산
    for c in node.child.values():
        res += dfs(node, c)

    # 버튼을 눌러야 할 횟수 반환
    return res
