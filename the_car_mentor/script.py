import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.car.info/en-se/bmw/1-series/116i-6711526/specs'

result = requests.get(url)
content = result.text

if result.status_code == 200:
    print('Conexión exitosa. Código de estado:', result.status_code)
else:
    print('Error al conectar a la página. Código de estado:', result.status_code)

soup = BeautifulSoup(content, 'lxml')

etiqueta_1 = soup.find_all('div', {'class': 'sprow ast-h sth-2'})
datos_etiqueta = []

for element in etiqueta_1:
    datos_etiqueta.append({'Elemento': element.text.strip()})
    print(element.text.strip())
    exit(0)

# Pasar resultado a DataFrame y luego a CSV
df = pd.DataFrame(datos_etiqueta)
resultado = 'resultado.csv'
df.to_csv(resultado, index=False, encoding='utf-8')

print(f'Los datos se han guardado en {resultado}')

