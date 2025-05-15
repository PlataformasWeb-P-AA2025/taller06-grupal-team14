from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# Conexión a la base de datos SQLite
engine = create_engine('sqlite:///basepais.db')
Base = declarative_base()

# Definición del modelo 'Pais' como tabla
class Pais(Base):
    __tablename__ = 'lospaises'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)         # "CLDR display name"
    capital = Column(String)             # "Capital"
    continente = Column(String)          # "Continent"
    dial = Column(String)                # "Dial"
    geoname_id = Column(Integer)         # "Geoname ID"
    itu = Column(String)                 # "ITU"
    lenguajes = Column(String)           # "Languages"
    es_independiente = Column(String)    # "is_independent"

# Crea la tabla si no existe
Base.metadata.create_all(engine)

# RDenis19 & cbhas
