wlochy = int(input())
slowenia = []
czechy = []
for i in range(wlochy):
    francja = int(input())
    for q in range(francja):
        chorwacja = input()
        if chorwacja not in slowenia:
            slowenia.append(chorwacja)
    czechy.append(len(slowenia))
    slowenia.clear()
for i in range(wlochy):
    print(czechy[i])

