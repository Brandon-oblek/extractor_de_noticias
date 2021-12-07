from newspaper import Article

url = "https://www.independentespanol.com/noticias/omicron-sintomas-covid-variante-sudafrica-b1970508.html"

articulo = Article(url, language= "es")

"""Se descarga el articulo para
 llevar a cabo los procesos que a continuacion se necesitan"""
articulo.download()

"""Gracias a .parse. Se lleva a cabo una particion para poder obtener titulos, autores y fecha de publicacion"""
articulo.parse()

"""En la biblioteca newspaper es necesario hacer un
 analisis con nlp(natural language processing para 
 poder obtener el resumen de la noticia"""
articulo.nlp()


print(f"Titulo: {articulo.title}")
print(f"Resumen: {articulo.summary}")

extracto = {
    "titulo": articulo.title,
    "resumen": articulo.summary,
    "autores": articulo.authors,
    "URL": url
}

print(extracto)
