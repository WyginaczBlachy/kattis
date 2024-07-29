def main(grid, R, C):
    message = []
    for row in range(R):
        for col in range(C):
            char = grid[row][col]
            if char != ".":
                message.append(char)
    return "".join(message)
def rozpierdol():
    R, C = map(int, input().split())
    grid = [input().strip() for _ in range(R)]
    secre_message = main(grid, R, C)
    print(secre_message)
rozpierdol()
