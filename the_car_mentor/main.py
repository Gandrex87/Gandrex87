import httpx
import pandas as pd
from selectolax.parser import HTMLParser

#1. Respuesta pagina web:
url = "https://www.carros.com/autos-en-venta/audi-br183-co243/"
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

resp = httpx.get(url , headers=headers)
html = HTMLParser (resp.text)
#print(html.css_first('title').text())

#2.Buscar etiquetas dentro de la web:
products = html.css(".post-information-wrapper")
#print(products)

#funcion en caso de encontrar una etiqueta vacia NO genere error:
def extract_text(html , sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

#3. crear dic{}
datos=[]
for product in products:
    item = {
        'name_&_model':extract_text(product , ".post-item-title"),
        'price' : extract_text(product , '.price-value'),
    }
    datos.append(item)
    print(item)
    
# 4. Guardar informacion en csv:
df = pd.DataFrame(datos)
nombre_archivo ='modelo_precio.csv'
df.to_csv(nombre_archivo, index=False)

print(f'los resultados se han guardado en {nombre_archivo}')

