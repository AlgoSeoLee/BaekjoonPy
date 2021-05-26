from sys import stdin
from bisect import bisect_left

def compressed_A_and_set_B(plain_A, plain_B):
    compressed_A = ''
    set_B = {}

    for current_A in plain_A:
        is_duplicate = False
        index_array_of_B = set_B.get(current_A)
        if index_array_of_B:
            is_duplicate = True
            latest_index = index_array_of_B[-1]
            if latest_index:
                new_index = plain_B[latest_index+1:].index(current_A)
                new_index += latest_index + 1
                index_array_of_B.append(new_index)
        else:
            index_of_plain_B = None
            try:
                index_of_plain_B = plain_B.index(current_A)
            except ValueError:
                pass

            if index_of_plain_B != None:
                is_duplicate = True
                set_B.update({current_A: [index_of_plain_B]})
            
        if is_duplicate:
            compressed_A += current_A

    for key_B in set_B:
        index_array = set_B[key_B]
        index = index_array[-1]
        slice_B = plain_B[index+1:]
        while True:
            try:
                index += slice_B.index(key_B) + 1
                index_array.append(index)
                slice_B = plain_B[index+1:]
            except ValueError:
                break


    return (compressed_A, set_B)

def generate_substring(compressed_A, set_B):
    maximum_substring = ''
    maximum_length = 0
    for start_A in range(len(compressed_A)):
        substring = ''
        minimum_B = 0

        for current_A in compressed_A[start_A:]:
            index_B = bisect_left(set_B[current_A], minimum_B)
            try: 
                index_B = set_B[current_A][index_B]
            except:
                continue

            if index_B > minimum_B or minimum_B == 0:
                minimum_B = index_B
                if minimum_B == 0:
                    minimum_B += 1
                substring += current_A

        length_of_substring = len(substring)
        if length_of_substring > maximum_length:
            maximum_substring = substring
            maximum_length = length_of_substring

    return maximum_substring

plain_A = stdin.readline().rstrip()
plain_B = stdin.readline().rstrip()

compressed_A, set_B = compressed_A_and_set_B(plain_A, plain_B)
print(compressed_A, set_B)
print(generate_substring(compressed_A, set_B))

