n = int(input())
for i in range(n + 1):
    spaces_before = ' ' * (n + 1 - i)
    if i == 0:
        print(spaces_before + 'x')
    else:
        inner_spaces = ' ' * (2 * i - 1)
        print(spaces_before + '/' + inner_spaces + '\\')

middle_spaces = ' ' * (2 * n + 1)
print('x' + middle_spaces + 'x')

for i in range(n, -1, -1):
    spaces_before = ' ' * (n + 1 - i)
    if i == 0:
        print(spaces_before + 'x')
    else:
        inner_spaces = ' ' * (2 * i - 1)
        print(spaces_before + '\\' + inner_spaces + '/')
