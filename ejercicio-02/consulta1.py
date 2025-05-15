from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from generar_base import Pais

# Conexión a la base de datos y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 1. Países de Norteamérica
paises = session.query(Pais).filter(Pais.continente == 'NA').all()
for p in paises:
    print(p.nombre_pais, "-", p.continente)

# RDenis19 & cbhas
