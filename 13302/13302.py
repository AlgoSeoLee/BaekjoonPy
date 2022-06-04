from sys import stdin

def calc_minimum_resort_cost(rest_day, coupon):
    if len(rest_day) == 0:
        return 0
    elif rest_day[0]:
        return min([
            37 + calc_minimum_resort_cost(rest_day[5:], coupon + 2),
            25 + calc_minimum_resort_cost(rest_day[3:], coupon + 1),
            10 + calc_minimum_resort_cost(rest_day[1:], coupon) if coupon < 3 else calc_minimum_resort_cost(rest_day[1:], coupon - 3)
        ])
    return calc_minimum_resort_cost(rest_day[1:], coupon)

num_of_days, _ = map(int, stdin.readline().split())
days = [True for _ in range(num_of_days)]
for schedule in map(int, stdin.readline().split()):
    days[schedule - 1] = False

print(calc_minimum_resort_cost(days, 0))
