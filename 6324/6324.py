from sys import stdin
import re

"https://www.acmicpc.net/problem/6324 URLs <Silver I>"

url_scheme = re.compile(r"(\w+)://([\w\d\.\_-]+)(:\d+)?(/.+)?")
DEFAULT = " <default>"

def url_parsing(url):
    protocol, host, port, path = url_scheme.match(url).groups()
    if port is None:
        port = DEFAULT
    if path is None:
        path = DEFAULT

    return {
        "Protocol": protocol,
        "Host": host,
        "Port": port[1:],
        "Path": path[1:],
    }

num_of_urls = int(stdin.readline())
for i in range(num_of_urls):
    url = stdin.readline().rstrip()
    result = url_parsing(url)

    print(f'URL #{i+1}')
    for k in result:
        print(f'{k:8} = {result[k]}')
    print()
