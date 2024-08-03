qtaz = int(input())
puzzy = [input().strip() for _ in range(qtaz)]
szukane = ["phone", "keys", "wallet"]
szukane_alt = sorted(szukane)
zabrane = True
for item in szukane_alt:
    if item not in puzzy:
        print(item)
        zabrane = False
if zabrane:
    print('ready')
