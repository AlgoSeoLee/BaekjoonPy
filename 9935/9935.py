from sys import stdin

plain = stdin.readline().rstrip()
plain_length = len(plain)
trigger = stdin.readline().rstrip()
rev_trigger = trigger[::-1]
trigger_length = len(trigger)

current = 0
while current < plain_length:
    print(current)
    if plain[current] == trigger[0]:
        stack = []
        start = current
        while current < plain_length:
            if plain[current] in trigger:
                stack.append(plain[current])
                current += 1
            else:
                break

        print(stack)

        count = 0
        after = ''
        while stack:
            elem = stack.pop()
            print(elem, rev_trigger[count])
            if elem == rev_trigger[count]:
                count += 1
                after = elem + after
                if count == trigger_length:
                    after = after[:len(after) - count]
            elif count > 0:
                count = 0
                if rev_trigger[0] == elem:
                    count = 1
                after = elem + after
            else:
                after = elem + after
                while stack:
                    after = stack.pop() + after

        plain_length -= current - start - len(after)
        plain = plain[:start] + after + plain[current:]
        print(plain)
        current = start

    current += 1

print(plain)
