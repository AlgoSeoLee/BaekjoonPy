from sys import stdin

magic_word = stdin.readline().rstrip()
length_of_magic_word = len(magic_word)

bridges = {state: stdin.readline().rstrip() for state in [True, False]}
length_of_bridges = len(bridges[0])

dp = {True: [], False: []}
def sum_bridges_way(bridges, state, index_of_bridge, index_of_character):
    area = dp[state] 
    if index_of_bridge != length_of_bridges:
        area = dp[state][0:index_of_bridge]
    return sum(
        map(
            lambda cases: cases[index_of_character],
            area
        )
    )

for index_of_bridge in range(0, length_of_bridges):
    for state in [True, False]:
        dp[state].append([0 for _ in range(length_of_magic_word)])
        for index_of_character, character in enumerate(magic_word):
            way = 0
            if bridges[state][index_of_bridge] == character:
                if index_of_character != 0:
                    other_side = sum_bridges_way(
                        bridges,
                        not state,
                        index_of_bridge,
                        index_of_character - 1
                    )
                    way += other_side
                else:
                    way = 1

            dp[state][index_of_bridge][index_of_character] = way

print(
    sum_bridges_way(bridges, True, length_of_bridges, length_of_magic_word - 1) +
    sum_bridges_way(bridges, False, length_of_bridges, length_of_magic_word - 1))
