n = int(input())
phone_book = {}

for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

import sys
for line in sys.stdin:
    q = line.strip()
    if q in phone_book:
        print(f"{q}={phone_book[q]}")
    else:
        print("Not found")
