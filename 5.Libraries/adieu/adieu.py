import inflect

p = inflect.engine()
list = []

while True:
    try:
        x = input("Name: ")
        list.append(x)
    except EOFError:
        break

if len(list) >= 1:
    op = p.join(list)
    print("Adieu, adieu, to", op)

