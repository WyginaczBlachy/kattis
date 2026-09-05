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
    hmm = [A[0], A[1], A[2]]
    hmmm = sorted(hmm)
    print(hmmm[1])
elif t == 4:
    print(sum(A))
elif t == 5:
    B = []
    for piece in A:
        if piece % 2 == 0:
            B.append(piece)
    print(sum(B))
elif t == 6:
    burger = [num % 26 for num in A]
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    pizza = "".join(alfabet[i] for i in burger)
    print(pizza)
else:
    index = 0
    monke = set()

    while True:
        if index < 0 or index >= N:
            print("Out")
            break

        if index == N - 1:
            print("Done")
            break

        if index in monke:
            print("Cyclic")
            break

        monke.add(index)
        index = A[index]