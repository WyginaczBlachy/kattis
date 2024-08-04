
N, t = map(int, input().split())
A = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t == 3:
    eskortka = [A[0], A[1], A[2]]
    striptizerka = sorted(eskortka)
    print(striptizerka[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    B = []
    for traktor in A:
        if traktor % 2 == 0:
            B.append(traktor)
    print(sum(B))
elif t == 6:
    katarzyna = [num % 26 for num in A]
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    marcelina = "".join(alfabet[i] for i in katarzyna)
    print(marcelina)
else:
    index = 0
    oral = set()

    while True:
        if index < 0 or index >= N:
            print("Out")
            break

        if index == N - 1:
            print("Done")
            break

        if index in oral:
            print("Cyclic")
            break

        oral.add(index)
        index = A[index]
