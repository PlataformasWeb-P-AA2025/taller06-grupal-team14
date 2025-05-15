from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from generar_base import Pais

# Conexión a la base de datos y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 2. Países de Asia ordenados por código de marcado (dial)
paises = session.query(Pais).filter(Pais.continente == 'AS').order_by(Pais.dial).all()
for p in paises:
    print(p.nombre_pais, "-", p.dial)

# RDenis19 & cbhas
