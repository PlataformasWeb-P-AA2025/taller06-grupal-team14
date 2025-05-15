import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from generar_base import Pais  # Importa la clase Pais desde el archivo con el modelo

# Conexión a la base de datos y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# Descarga del JSON con los datos de países
response = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")
datos_json = response.json()

# Carga de datos a la base
for item in datos_json:
    pais = Pais(
        nombre_pais=item.get("CLDR display name"),
        capital=item.get("Capital"),
        continente=item.get("Continent"),
        dial=item.get("Dial"),
        geoname_id=item.get("Geoname ID"),
        itu=item.get("ITU"),
        lenguajes=item.get("Languages"),
        es_independiente=item.get("is_independent")
    )
    session.add(pais)

session.commit()  # Guarda todos los cambios

# RDenis19 & cbhas
