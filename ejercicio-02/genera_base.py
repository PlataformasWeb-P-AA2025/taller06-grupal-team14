from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///basepais.db')
Base = declarative_base()

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

Base.metadata.create_all(engine)