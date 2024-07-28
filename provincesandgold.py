class VictoryCards:

    def __init__(self, name, cost, victory_points):
        self.cost = cost
        self.victory_points = victory_points
        self.name = name


class TreasureCards:
    def __init__(self, name, costs, buying_power):
        self.name = name
        self.costs = costs
        self.buying_power = buying_power

g, s, c = map(int, input().split())

Province = VictoryCards("Province", 8, 6)
Duchy = VictoryCards("Duchy", 5, 3)
Estate = VictoryCards("Estate", 2, 1)
Gold = TreasureCards("Gold", 6, 3)
Silver = TreasureCards("Silver", 3, 2)
Copper = TreasureCards("Copper", 0, 1)

VCards = [Province, Duchy, Estate]
TCards = [Gold, Silver, Copper]

buy_power = Gold.buying_power*g + Silver.buying_power*s + Copper.buying_power*c

available_VC = 0
available_TC = 0
for card in VCards:
    if buy_power >= card.cost:
        available_VC = card
        break
for card in TCards:
    if buy_power >= card.costs:
        available_TC = card
        break
if available_TC and available_VC:
    print(f"{available_VC.name} " + "or " + f"{available_TC.name}")
else:
    print(f"{available_TC.name}")
