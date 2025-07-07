import pandas as pd
import requests
from io import StringIO
import streamlit as st

def leer_csv_desde_url(url, sep=',', encoding='utf-8'):
    try:
        response = requests.get(url)
        response.raise_for_status() # Lanza una excepción para códigos de estado HTTP 4xx/5xx
        content = response.content.decode(encoding)
        csv_data = StringIO(content)
        df = pd.read_csv(csv_data, sep=sep)
        return df

    except requests.exceptions.RequestException as e:
        raise Exception(f"Error de red o al acceder a la URL: {e}")
    except pd.errors.EmptyDataError:
        raise Exception("Error: El archivo CSV está vacío o solo contiene encabezados.")
    except pd.errors.ParserError as e:
        raise Exception(f"Error de análisis CSV. Revisa el delimitador (sep) o el formato del archivo: {e}")
    except Exception as e:
        raise Exception(f"Ocurrió un error inesperado: {e}")
    
url = "https://drive.google.com/uc?export=download&id=1UyX7sRATSNbadNxUZ7AAmbeOUm7sVpGF"

df = leer_csv_desde_url(url)

magnitud = df[df["Magnitude"]== df["Magnitude"].max()]

magnitud_valor = list(magnitud["Magnitude"])[0]

magnitud_year = list(magnitud["Year"])[0]

magnitud_ubicacion = list(magnitud["Location_Name"])[0]

muertes = df[df["Death"]== df["Death"].max()]

muertes_valor = list(muertes["Death"])[0]

muertes_year = list(muertes["Year"])[0]

muertes_ubicacion = list(muertes["Location_Name"])[0]

daño = df[df["Damage"]== df["Damage"].max()]

daño_valor = list(daño["Damage"])[0]

daño_year = list(daño["Year"])[0]

daño_ubicacion = list(daño["Location_Name"])[0]

c1, c2, c3 = st.columns(3)
c1.metric(f"Mayor Magnitud: {str(magnitud_year)}",magnitud_valor,magnitud_ubicacion)
c2.metric(f"Mayores Muertes: {str(muertes_year)}",muertes_valor, f"-{muertes_ubicacion}")
c3.metric(f"Mayor daño: {str(daño_year)}",daño_valor,f"-{daño_ubicacion}")