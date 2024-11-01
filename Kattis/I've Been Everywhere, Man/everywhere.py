kocham = int(input())
piekne = []
ladne = []
for i in range(kocham):
     kobiety = int(input())
     for q in range(kobiety):
         sliczne = input()
         if sliczne not in piekne:
             piekne.append(sliczne)
     ladne.append(len(piekne))
     piekne.clear()
for i in range(kocham):
    print(ladne[i])
    