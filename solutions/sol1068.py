import sys

input = sys.stdin.readline


# 1068 트리
# n개의 노드로 구성된 트리에서 노드 하나와 그 서브트리를 지웠을 때
# 리프노드의 갯수를 구하는 문제 
def sol1068():
    n = int(input())
    tree = list(map(int, input().split()))
    removed = int(input())

    # 제거된 노드의 부모노드 -1로 변경
    tree[removed] = -1

    # 모든 노드중 부모노드로 언급된 노드를 리프노드 후보에서 제거
    cand = set(range(n))
    for p in tree:
        cand.discard(p)

    # 리프노드 후보중 부모에 제거된 노드가 있는 노드를 제외한 수를 세어 반환
    answer = 0
    for node in cand:
        if node == removed:
            continue
        isLeaf = True
        while tree[node] >= 0:
            node = tree[node]
            if node == removed:
                isLeaf = False
                break
        if isLeaf:
            answer += 1
    return answer
