import requests
from bs4 import BeautifulSoup
import pandas as pd


def car_info(element):
    result = requests.get(element)
    content = result.text

    if result.status_code == 200:
        print('Conexión exitosa. Código de estado:', result.status_code)
    else:
     print('Error al conectar a la página. Código de estado:', result.status_code)

    soup = BeautifulSoup(content, 'lxml')

    etiqueta_1 = soup.find_all('div', {'class': 'sprow'})
    datos_etiqueta = []

    for element in etiqueta_1:
        datos_etiqueta.append({'Elemento': element.text.strip()})

    # Pasar resultado a DataFrame y luego a CSV
    df = pd.DataFrame(datos_etiqueta)
    resultado = 'resultado.csv'
    df.to_csv(resultado, index=False, encoding='utf-8')

    print(f'Los datos se han guardado en {resultado}')

def km_77(element):
    result = requests.get(element)
    content = result.text

    if result.status_code == 200:
        print('Conexión exitosa. Código de estado:', result.status_code)
    else:
        print('Error al conectar a la página. Código de estado:', result.status_code)

    soup = BeautifulSoup(content, 'lxml')

    etiqueta_1 = soup.find_all(['th','td'])
    datos_etiqueta = []

    for element in etiqueta_1:
        datos_etiqueta.append({'resultadoKM77': element.text.strip()})
        print(element)

    # Pasar resultado a DataFrame y luego a CSV
    df = pd.DataFrame(datos_etiqueta)
    resultado = 'resultadokm77.csv'
    df.to_csv(resultado, index=False, encoding='utf-8')

    print(f'Los datos se han guardado en {resultado}')


car_info('https://www.car.info/en-se/bmw/1-series/118i-3-door-m6-2010-33387/specs')

