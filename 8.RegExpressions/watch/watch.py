import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Patrón de expresión regular para buscar la URL de YouTube en el atributo src de un elemento iframe
    pattern = r'<iframe [^>]*?src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))".*?</iframe>'

    # Buscar la coincidencia en la cadena de entrada
    match = re.search(pattern, s)

    # Verificar si se encontró una coincidencia
    if match:
        # Obtener la URL de YouTube y convertirla a formato youtu.be
        youtube_url = match.group(1)
        #print(f"Ver: {youtube_url}")
        video_id = match.group(2)
        #print(video_id)
        shortened_url = f"https://youtu.be/{video_id}"
        return shortened_url
    else:
        return "None"

if __name__ == "__main__":
    main()
