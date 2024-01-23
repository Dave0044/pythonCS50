dict = {}
while True:
    try:
        item = input()
        item = item.upper()
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    except EOFError:
        break
for item in sorted(dict):
    print(dict[item], item)
