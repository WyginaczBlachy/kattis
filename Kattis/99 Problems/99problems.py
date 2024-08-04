
N = int(input())
if N < 148:
    print(99)
else:
    ostatnia = N % 100
    if ostatnia < 49:
        print(int(str(int(N/100)-1) + "99"))
    else:
        print(int(str(int(N/100)) + "99"))
