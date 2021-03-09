from sys import stdin

"https://www.acmicpc.net/problem/1620 나는야 포켓몬 마스터 이다솜 <실버 4>"

pocketmon_by_number = []
pockedex_by_name = {}

number_of_monster, number_of_question = map(int, stdin.readline().split())
for n in range(number_of_monster):
    pocketmon_name = stdin.readline().rstrip()
    pocketmon_by_number.append(pocketmon_name)
    pockedex_by_name[pocketmon_name] = n + 1

for _ in range(number_of_question):
    question = stdin.readline().rstrip()
    try:
        number = int(question) - 1
        print(pocketmon_by_number[number])
    except ValueError:
        print(pockedex_by_name[question])
