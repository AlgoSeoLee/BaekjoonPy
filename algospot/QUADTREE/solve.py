from sys import stdin,setrecursionlimit

setrecursionlimit(10**7)

def parse_quadtree(plain, start=0, limit=1):
    current = start
    length_of_plain = len(plain)
    quadtree = []
    count_of_object = 0

    while current < length_of_plain and count_of_object < limit:
        if plain[current] == 'x':
            (result, next_current) = parse_quadtree(plain, current+1, 4)
            quadtree.append([result[0:2], result[2:4] ,True])
            current = next_current
        else:
            quadtree.append(plain[current])
            current += 1

        count_of_object += 1

    return (quadtree, current)

def reverse_y_axis_quadtree(quadtree):
    reversed_quadtree = []
    for subtree in quadtree[0:2]:
        if type(subtree) is list:
            reversed_quadtree.append(reverse_y_axis_quadtree(subtree))
        else:
            reversed_quadtree.append(subtree)

    try:
        if quadtree[2]:
            reversed_quadtree.reverse()
            reversed_quadtree.append(True)

    except:
        pass

    return reversed_quadtree

def quadtree_to_string(quadtree):
    result = ''
    for subtree in quadtree[0:2]:
        if type(subtree) is str:
            result += subtree
        else:
            result += quadtree_to_string(subtree)

    try:
        if quadtree[2]:
            return 'x' + result
    except:
        pass
        
    return result

num_of_test_case = int(stdin.readline())
for _ in range(num_of_test_case):
    (result, _) = parse_quadtree(stdin.readline())
    result = reverse_y_axis_quadtree(result)
    print(quadtree_to_string(result))
