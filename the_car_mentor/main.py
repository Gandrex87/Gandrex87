import httpx
import pandas as pd
from selectolax.parser import HTMLParser
import time

#1. Respuesta pagina web:

def get_html(baseurl , page):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
    resp = httpx.get(baseurl + str(page) , headers=headers , follow_redirects=True)
    html = HTMLParser (resp.text)
    return html

def extract_text(html , sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

def parse_page(html):
    products = html.css(".post-information-wrapper")
        
    for product in products:
        item = {
            'name_&_model':extract_text(product , ".post-item-title"),
            'price' : extract_text(product , '.price-value'),
        }
        yield item
        #print(item)
           
def main():
    baseurl = "https://www.carros.com/autos-en-venta/audi-br183-co243/?page="
    for x in range(1,1):
        print(f'compilando pagina: {x}')
        html =get_html(baseurl, x)
        data = parse_page(html)
        for item in data:
            print(item)
        time.sleep(1)   
        
         
# 4. Guardar informacion en csv:
    #df = pd.DataFrame(item)
    #nombre_archivo ='modelo_precio.csv'
    #df.to_csv(nombre_archivo, index=False)

    #print(f'los resultados se han guardado en {nombre_archivo}')

if __name__ == "__main__":
    main()
