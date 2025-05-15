from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from generar_base import Pais

# Conexión a la base de datos y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 4. Capitales de Europa ordenadas alfabéticamente junto con el país
paises = session.query(Pais).filter(Pais.continente == 'EU').order_by(Pais.capital).all()
for p in paises:
    print(p.capital, "-", p.nombre_pais)

# RDenis19 & cbhas
