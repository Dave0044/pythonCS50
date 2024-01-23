import re
import sys


def main():
    x = input("IPv4 Address: ")
    print(validate(x))


def validate(ip):
    # Patrón de expresión regular para validar IPv4
    ipv4_pattern = re.compile(
        r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    )

    # Intentar hacer coincidir el patrón con la dirección IP proporcionada
    match = ipv4_pattern.match(ip)

    if match:
        # Las partes de la dirección IPv4
        octet1, octet2, octet3, octet4 = map(int, match.groups())

        # Verificar si cada octeto está en el rango correcto (0-255)
        if 0 <= octet1 <= 255 and 0 <= octet2 <= 255 \
                and 0 <= octet3 <= 255 and 0 <= octet4 <= 255:
            return True

    # La dirección IP no es válida
    return False


if __name__ == "__main__":
    main()
