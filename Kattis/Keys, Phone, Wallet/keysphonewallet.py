obiad = int(input())
pizza= [input().strip() for _ in range(obiad)]
szukane = ["phone", "keys", "wallet"]
szukane_alt = sorted(szukane)
zabrane = True
for item in szukane_alt:
    if item not in pizza:
        print(item)
        zabrane = False
if zabrane:
    print('ready')
