from sys import stdin
from heapq import heappop, heappush

"https://www.acmicpc.net/problem/11286 절댓값 힙 <Silver I>"

class ABSHeap:
    def __init__(self):
        self.heap = []
        self.elem = {}

    def push(self, e):
        heappush(self.heap, abs(e))
        if not self.elem.get(e):
            self.elem[e] = 0
        self.elem[e] += 1

    def pop(self):
        try:
            plus = heappop(self.heap)
            minus = plus * -1
            if self.elem.get(minus) != None and self.elem[minus] > 0:
                self.elem[minus] -= 1
                return minus
            else:
                self.elem[plus] -= 1
                return plus
        except IndexError:
            pass

        return 0

num_of_case = int(stdin.readline())
heap = ABSHeap()
for _ in range(num_of_case):
    elem = int(stdin.readline())
    if elem == 0:
        print(heap.pop())
    else:
        heap.push(elem)
