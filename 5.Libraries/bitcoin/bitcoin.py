import requests
import json
import sys

def decimal(x):
    try:
        x = float(x)
        return x
    except ValueError:
        sys.exit("Command-line argument is not a number")

def agregar_punto_despues_coma(n):
    m1 = ''
    coma_encontrada = False
    contador = 0

    for c in n:
        if c == ',':
            coma_encontrada = True
            contador = 0
            m1 += c
        else:
            if coma_encontrada:
                if contador == 3:
                    m1 += '.'
                    coma_encontrada = False
                else:
                    contador += 1
            m1 += c

    return m1

def main():
    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        elif len(sys.argv) > 2:
            sys.exit("Only one command-line")
        else:
            y = decimal(sys.argv[1])
            res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            data = res.json()
            json.dumps((data), indent=2)
            usd_rate = data["bpi"]["USD"]["rate"]
            usd_rate = float(usd_rate.replace(",", ""))
            m = y * usd_rate/1000
            m = "{:,.7f}".format(m).replace('.', ',')
            m1 = agregar_punto_despues_coma(m)
            print(f"${m1}")
    except requests.RequestException:
        pass

main()
