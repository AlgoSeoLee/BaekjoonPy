from sys import stdin

"https://www.acmicpc.net/problem/18870 좌표 압축 <Silver II>"

length_coordinate = int(stdin.readline())
coordinates = list(map(int, stdin.readline().split()))

index_of_coordinate = sorted(set(coordinates))
map_of_coordinate = {}
map_of_coordinate.update(
    zip(index_of_coordinate, range(len(index_of_coordinate)))
)
result = map(lambda coord: map_of_coordinate[coord], coordinates)
for i in result:
    print(i, end=" ")
print()
