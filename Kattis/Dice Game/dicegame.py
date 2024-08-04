A, B, C, D = map(int, input().split())
gunnar_dice_one = []
gunnar_dice_two = []

for i in range(B+1):
    if i >= A:
        gunnar_dice_one.append(i)
for i in range(D+1):
    if i >= C:
        gunnar_dice_two.append(i)

E, F, G, H = map(int, input().split())
emma_dice_one = []
emma_dice_two = []

for i in range(F+1):
    if i >= E:
        emma_dice_one.append(i)
for i in range(H+1):
    if i >= G:
        emma_dice_two.append(i)

gunnar_average_roll = float(sum(gunnar_dice_one)/len(gunnar_dice_one)) + float((sum(gunnar_dice_two)/len(gunnar_dice_two)))
emma_average_roll = float(sum(emma_dice_one)/len(emma_dice_one)) + float((sum(emma_dice_two)/len(emma_dice_two)))

if gunnar_average_roll > emma_average_roll:
    print("Gunnar")
elif gunnar_average_roll < emma_average_roll:
    print("Emma")
elif gunnar_average_roll == emma_average_roll:
    print("Tie")
