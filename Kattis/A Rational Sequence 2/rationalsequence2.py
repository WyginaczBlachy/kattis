P = int(input())
for i in range(P):
    [K, p, q] = (int(_) for _ in input().replace(' ', '/').split('/'))
    binary = ''
    while p > 1 or q > 1:
        if p > q:
            binary += '1'
            p -= q
        else:
            binary += '0'
            q -= p
    binary += '1'

    n = sum([(2**i) * int(binary[i]) for i in range(len(binary))])
    print(K, n)