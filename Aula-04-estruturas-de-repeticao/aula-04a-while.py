num = 0

while num < 10:
    num += 1

    if num == 3 or num == 5:
        continue

    if num == 7:
        break

    print(f"produto {num}")


i = 4

while i > 0:
    print(f"produto {i}")
    i -= 1