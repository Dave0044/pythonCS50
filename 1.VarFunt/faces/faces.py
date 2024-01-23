def convert(x):
    x = x.replace(":)", "🙂").replace(":(", "🙁")
    print(x)

def main():
    n = input()
    n=convert(n)

main()
