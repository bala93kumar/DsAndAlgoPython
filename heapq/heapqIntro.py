
#  https://www.hackerrank.com/challenges/qheap1/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign



import heapq


d = {}

h = []

Q = int(input())

print("give the list of inputs")

result = []

for i in range(Q):
    l = [int(x) for x in input().strip().split(' ')]
    # print(len(l))
    a,b = l[0] ,l[1] if len(l) > 1 else None
    # print(a,b)
    # print(l[0])
    if a == 1 :
        heapq.heappush(h, b)
    elif a == 2:
        print(h[0])
    elif a == 3:
        heapq.heappop(h)
        print(h)


