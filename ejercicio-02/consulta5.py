from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from generar_base import Pais

# Conexión a la base de datos y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 5. Países cuyo nombre contiene 'uador' o cuya capital termina en 'ito'
paises = session.query(Pais).filter(
    or_(
        Pais.nombre_pais.like('%uador%'),
        Pais.capital.like('%ito%')
    )
).all()
for p in paises:
    print(p.nombre_pais, "-", p.capital)

# RDenis19 & cbhas
