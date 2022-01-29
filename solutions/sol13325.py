import sys

input = sys.stdin.readline


# 13325 이진 트리
# 높이 k의 포화이진트리의 루트노드부터 리프노드까지의 가중치의 합을
# 모두 같도록 하기 위해 최소한의 가중치만을 더한 뒤 모든 간선의 가중치의 합을 구하는 문제
def sol13325():
    k = int(input())
    tree = [0, *map(int, input().split())]
    n = len(tree)

    # 기존 간선의 가중치합
    answer = sum(tree)

    # 리프노드로부터 sibling 관계인 노드간의 차를 answer에 더하고
    # 둘중 큰쪽을 부모노드에 합산
    for i in range(n-1, 0,  -2):
        l, r = tree[i-1], tree[i]
        if l < r:
            l, r = r, l
        tree[(i-1)//2] += l
        answer += (l - r)
    return answer
