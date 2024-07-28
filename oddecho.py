def main():
    N = int(input())
    words = []
    for _ in range(N):
        word = input()
        words.append(word)
    for i in range(0, N, 2):
        print(words[i])

main()
