n = int(input())
names = []
for i in range(n):
    name = str(input())
    names.append(name)
sortednames = sorted(names)
reversednames = list(reversed(names))
if sortednames == names:
    print("increasing")
elif sortednames == reversednames:
    print("decreasing")
else:
    print("neither")
