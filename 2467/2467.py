from sys import stdin, maxsize

"https://www.acmicpc.net/problem/2467 용액 <Gold V>"

num_of_solution = int(stdin.readline())
solutions = [int(v) for v in stdin.readline().split()]

base = 0
additive = num_of_solution - 1

closest_mix = maxsize
closest_base = 0
closest_additive = num_of_solution - 1
while base != additive:
    mix = solutions[base] + solutions[additive]
    if abs(mix) <= closest_mix:
        closest_mix = abs(mix)
        closest_base = base
        closest_additive = additive

    if mix < 0:
        base += 1
    elif mix > 0:
        additive -= 1
    else:
        break

print(solutions[closest_base], solutions[closest_additive])
