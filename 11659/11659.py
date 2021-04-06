from sys import stdin

def get_integers():
    return map(int, stdin.readline().split())

_, num_of_question = get_integers()

numbers = stdin.readline().split()
for _ in range(num_of_question):
    start, end = get_integers()
    start -= 1

    result = 0
    for num in numbers[start:end]:
        result += int(num)

    print(result)
