eye = input()
bars = eye.split('()')


def check(bars):
    return len(set(bars)) == 1


if check(bars) is True:
    print("correct")
else:
    print("fix")