import random


def main():
    n = get_level()
    corr = generate_integer(n)
    print(f"Score: {corr}")

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x == 1 or x == 2 or x==3:
                break
            else:
                #print("Only three levels")
                continue
        except ValueError:
            #print("Only numerical values")
            continue
    return x

def generate_integer(x):
    corr = 0
    while True:
        try:
            if x == 1:
                for i in range(10):
                    na1 = random.randint(0, 9)
                    na2 = random.randint(0, 9)
                    try:
                        correct_answer = na1 + na2
                        for i in range(3):
                            r1 = int(input(f"{na1} + {na2} = "))
                            if r1 == na1 + na2:
                                print("Correct")
                                corr += 1
                                break
                            else:
                                print("EEE")
                                continue
                        else:
                            print(f"{na1} + {na2} = {correct_answer}")
                    except ValueError:
                        continue
                break
            elif x == 2:
                for i in range(10):
                    na1 = random.randint(10, 99)
                    na2 = random.randint(10, 99)
                    try:
                        correct_answer = na1 + na2
                        for i in range(3):
                            r1 = int(input(f"{na1} + {na2} = "))
                            if r1 == na1 + na2:
                                print("Correct")
                                corr += 1
                                break
                            else:
                                print("EEE")
                                continue
                        else:
                            print(f"{na1} + {na2} = {correct_answer}")
                    except ValueError:
                        continue
                break
            elif x == 3:
                for i in range(10):
                    na1 = random.randint(100, 999)
                    na2 = random.randint(100, 999)
                    try:
                        correct_answer = na1 + na2
                        for i in range(3):
                            r1 = int(input(f"{na1} + {na2} = "))
                            if r1 == na1 + na2:
                                print("Correct")
                                corr += 1
                                break
                            else:
                                print("Is not correct")
                                continue
                        else:
                            print(f"{na1} + {na2} = {correct_answer}")
                    except ValueError:
                        continue
                break
        except ValueError:
            continue
    return corr

if __name__ == "__main__":
    main()
