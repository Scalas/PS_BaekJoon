from typing import List
import sys

input = sys.stdin.readline
INF = 10 ** 9


class Node:
    def __init__(self, data: int, left_bound: int, right_bound: int, left_child=None, right_child=None):
        self.data: int = data
        self.left_bound: int = left_bound
        self.right_bound: int = right_bound
        self.left_child: Node = left_child
        self.right_child: Node = right_child
    
    # start 부터 end 사이의 구간에 속하는 수 중에서만 최솟값을 구하는 메소드
    def calculate(self, start: int, end: int):
        if self.right_bound < start or self.left_bound > end:
            return INF
        if self.left_bound >= start and self.right_bound <= end:
            return self.data
        return min(self.left_child.calculate(start, end), self.right_child.calculate(start, end))


class SegmentTree:
    def __init__(self, numbers: List[int]):
        self.root: Node = self.init_tree(init_data=numbers,
                                         start=0,
                                         end=len(numbers)-1)

    # init_data 로부터 Segment Tree를 생성하는 메소드
    def init_tree(self, init_data: List[int], start: int, end: int) -> Node:
        if start == end:
            return Node(data=init_data[start], left_bound=start, right_bound=end)

        mid = (end + start) // 2
        left_child: Node = self.init_tree(init_data=init_data, start=start, end=mid)
        right_child: Node = self.init_tree(init_data=init_data, start=mid + 1, end=end)

        cur_node = Node(data=min(left_child.data, right_child.data),
                        left_bound=start,
                        right_bound=end,
                        left_child=left_child,
                        right_child=right_child)
        return cur_node

    # start 부터 end 까지의 구간의 최솟값을 구하는 메소드
    def query(self, start: int, end: int):
        return self.root.calculate(start, end)


def sol10868():
    n, m = map(int, input().split())
    seg_tree = SegmentTree([int(input()) for _ in range(n)])
    answer = []
    for _ in range(m):
        s, e = map(int, input().split())
        answer.append(seg_tree.query(s - 1, e - 1))
    return '\n'.join(map(str, answer))
