from sys import stdin

num_of_password, num_of_site = map(int, stdin.readline().split())

password_book = {}
password_book.update(
    [stdin.readline().split() for _ in range(num_of_password)]
)
for _ in range(num_of_site):
    print(password_book[stdin.readline().rstrip()])

