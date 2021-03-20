import sys
import json
import re
import urllib.request
from bs4 import BeautifulSoup

NAME_RULE = r"(\d+)/\d+.py"
CLIENT_HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}

def search_solved_ac(problem):
    req = urllib.request.Request(
        url="https://solved.ac/search?query=" + str(problem), headers=CLIENT_HEADER)

    with urllib.request.urlopen(req) as result:
        return result.read().decode("utf-8")

def parse_solved_ac(problem):
    plain = search_solved_ac(problem)
    soup = BeautifulSoup(plain)
    rows = soup.find_all("div", {"class": "sticky-table-row"})
    for r in rows:
        cells = r.find_all("div", {"class": "sticky-table-cell"})
        try:
            number_cell = cells[0].span.a
            title_cell = cells[1].span.a
            if int(number_cell.span.text) == problem:
                tier = number_cell.img.attrs["alt"]
                address = number_cell.attrs["href"]
                title = title_cell.text
                return (address, title, tier)
        except ValueError:
            continue
        except AttributeError:
            continue

if __name__ == "__main__":
    adding_files = json.loads(sys.argv[1])
    for path in adding_files:
        is_solve = re.match(NAME_RULE, path)
        if not is_solve:
            continue

        print("commenting: " + path)
 
        regs = is_solve.regs[1]
        problem = int(path[regs[0]:regs[1]])

        address, title, tier = parse_solved_ac(problem)

        with open(path, "r+") as target:
            end_of_import = False
            where = 0
            code = None
            while not end_of_import:
                line = target.readline()
                if line.find("import") < 0:
                    end_of_import = True
                    where = target.tell()
                    code = target.read()

            target.seek(where)
            comment = '"{} {} <{}>"\n\n'.format(address, title, tier)
            target.write(comment)
            target.write(code)
