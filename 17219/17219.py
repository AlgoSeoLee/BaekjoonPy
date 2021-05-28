from sys import stdin

"https://www.acmicpc.net/problem/17219 비밀번호 찾기 <Silver IV>"

num_of_password, num_of_site = map(int, stdin.readline().split())

password_book = {}
password_book.update(
    [stdin.readline().split() for _ in range(num_of_password)]
)
for _ in range(num_of_site):
    print(password_book[stdin.readline().rstrip()])

