

# Crea

from urllib.request import urlopen

url = 'https://www.youtube.com/watch?v=sWtEYPva4A0&ab_channel=SamCisco'


# CODICE PER PRENDERE LA CATEGORIA DI UN VIDEO
html = urlopen(url).read()
if b"category" in html:
    a,sep,b = str(html).partition("category")
    video_category = b[3:].split('"')[0].replace("\\u0026","&")

