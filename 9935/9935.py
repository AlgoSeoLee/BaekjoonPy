from sys import stdin

plain = stdin.readline().rstrip()
plain_length = len(plain)
trigger = stdin.readline().rstrip()
trigger_length = len(trigger)

current = 0
while current < plain_length:
    if plain[current] == trigger[0]:
        stack = []
        count = 0
        same = 0
        while current + count < plain_length:
            position = current + count
            stack.append(plain[position])
            count += 1

            if plain[position] == trigger[same]:
                same += 1
                if same == trigger_length:
                    same = 0
                    for _ in range(trigger_length):
                        stack.pop()
            elif plain[position] in trigger:
                same = 0
                if plain[position] == trigger[0]:
                    same = 1
            else:
                count -= 1
                stack.pop()
                break

        after = len(stack) - count
        plain_length += after
        plain = plain[:current] + ''.join(stack) + plain[current+count:]
    else:
        current += 1

if plain == '':
    print("FRULA")
else:
    print(plain)
