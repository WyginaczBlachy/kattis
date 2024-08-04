def jebanie(list):
    list = input().split()
    seen = []
    for word in list:
        if word in seen:
            return True
        seen.append(word)
    return False

if jebanie(list) is True:
    print("no")
else:
    print("yes")
