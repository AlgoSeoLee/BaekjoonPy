from sys import stdin

template = "wolf"
template_len = len(template)

word = stdin.readline().rstrip()

state = 0
threshold = 0
duplicate = 0
is_verify = '1'
for c in word:
    print(c, template[state], threshold, duplicate)
    if state == 0 and c == 'w':
        duplicate += 1
    elif state == 0 and duplicate > 0 and c == 'o':
        threshold = duplicate
        if threshold == 1:
            state = 2
            duplicate = 0
        else:
            state = 1
            duplicate = 1
    elif duplicate < threshold and template[state] == c:
        duplicate += 1
        if duplicate == threshold:
            duplicate = 0
            state += 1
            if state == template_len:
                state = 0
    elif state != 0:
        is_verify = '0'
        break

print(is_verify)
