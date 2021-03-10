import sys
import json
import re

NAME_RULE = r"(\d+)/\d+.py"

adding_files = json.loads(sys.argv[1])
for path in adding_files:
    is_solve = re.match(NAME_RULE, path)
    if not is_solve:
        continue

    regs = is_solve.regs[1]
    problem = int(path[regs[0]:regs[1]])

    print("commenting: " + path)
    with open(path, "w") as target:
        end_of_import = 0
        where = 1
        while end_of_import == 0:
            line = target.readline()
            if line.find('import') <= 0:
                end_of_import = where
            else:
                where = where + 1
