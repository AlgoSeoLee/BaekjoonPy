from sys import stdin,setrecursionlimit

setrecursionlimit(10**7)

def parse_quadtree(plain, start=0, limit=1):
    current = start
    length_of_plain = len(plain)
    quadtree = []
    count_of_object = 0

    while current < length_of_plain and count_of_object < limit:
        if plain[current] == 'x':
            (result, next_current) = parse_quadtree(plain, current + 1, 4)
            quadtree.append(result)
            current = next_current
        else:
            quadtree.append(plain[current])
            current += 1

        count_of_object += 1

    if count_of_object == 4:
        quadtree = [quadtree[0:2], quadtree[2:]]

    return (quadtree, current)

def reverse_y_axis_quadtree(quadtree):
    is_all_line = True
    for subtree in quadtree:
        if type(subtree) is list:
            reverse_y_axis_quadtree(subtree)
        else:
            is_all_line = False

    if is_all_line:
        quadtree.reverse()

def quadtree_to_string(quadtree):
    result = ''
    is_all_line = True
    count = 0
    for subtree in quadtree:
        count += 1
        if type(subtree) is str:
            is_all_line = False
            result += subtree
        else:
            result += quadtree_to_string(subtree)

    if count == 2 and is_all_line:
        return 'x' + result
        
    return result


(result, _) = parse_quadtree('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb')
print(result)
reverse_y_axis_quadtree(result)
print(result)
print(quadtree_to_string(result))
