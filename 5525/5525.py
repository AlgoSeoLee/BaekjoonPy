from sys import stdin

"https://www.acmicpc.net/problem/5525 IOIOI <Silver II>"

def _calc_partial_match(search):
    length_of_search = len(search)
    partial_match = [0 for _ in range(length_of_search)]

    begin = 1
    match = 0
    while begin + match < length_of_search:
        if search[begin + match] == search[match]:
            match += 1
            partial_match[begin + match - 1] = match
        elif match == 0:
            begin += 1
        else:
            begin += match - partial_match[match - 1]
            match = partial_match[match - 1]

    return partial_match

def kmp_search(plain, search):
    length_of_plain = len(plain)
    length_of_search = len(search)

    partial_match = _calc_partial_match(search)
    begin = 0
    match = 0
    result = 0
    limit = length_of_plain - length_of_search
    while begin <= limit:
        is_same = match < length_of_search
        is_same = is_same and plain[begin + match] == search[match]
        if is_same:
            match += 1

            if match == length_of_search:
                result += 1
        elif match == 0:
            begin += 1
        else:
            offset = partial_match[match - 1]
            begin += match - offset
            match = offset

    return result

num_of_O = int(stdin.readline())
length_of_plain = int(stdin.readline())
plain = stdin.readline()

search = 'I' + 'OI' * num_of_O

print(kmp_search(plain, search))

