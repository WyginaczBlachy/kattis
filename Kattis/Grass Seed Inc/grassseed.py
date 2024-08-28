seed_cost = float(input())
lawns = int(input())
widths = []
lengts = []
sum_all = []
for i in range(lawns):
    x, y = map(float, input().split())
    widths.append(x)
    lengts.append(y)
    suma = widths[i] * lengts[i]
    sum_all.append(suma)

print(sum(sum_all)*seed_cost)

