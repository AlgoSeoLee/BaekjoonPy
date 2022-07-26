from sys import stdin

result_plain = [
    list(map(int, stdin.readline().rstrip().split())) for _ in range(4)
]

for league_result_plain in result_plain:
    league_win_total = 0
    league_draw_total = 0
    league_lose_total = 0
    league_draw_team = 0

    for country in range(0, 18, 3):
        league = league_result_plain[country:country+3]
        print(league)

        league_win_total += league[0]
        if league[1] != 0:
            league_draw_total += league[1]
            league_draw_team += 1
        league_lose_total += league[2]

    if league_win_total == league_lose_total and league_draw_team == league_draw_total / 2:
        print(1)
    else:
        print(0)

