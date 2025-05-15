from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from generar_base import Pais

# Conexión a la base de datos y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 3. Listar cada país con sus lenguajes
paises = session.query(Pais).all()
for p in paises:
    print(p.nombre_pais, "->", p.lenguajes)

# RDenis19 & cbhas
