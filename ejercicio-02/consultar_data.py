from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

# Crear motor y sesión
engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 1. Países de Norteamérica
paises = session.query(Pais).filter(Pais.continente == 'NA').all()
for p in paises:
    print(p.nombre_pais, "-", p.continente)

print("/////////////////////////////////////////////////////////////////////////////////////")

# 2. Países de Asia ordenados por código de marcado (dial)
paises = session.query(Pais).filter(Pais.continente == 'AS').order_by(Pais.dial).all()
for p in paises:
    print(p.nombre_pais, "-", p.dial)

print("/////////////////////////////////////////////////////////////////////////////////////")

# 3. Listar cada país con sus lenguajes
paises = session.query(Pais).all()
for p in paises:
    print(p.nombre_pais, "->", p.lenguajes)

print("/////////////////////////////////////////////////////////////////////////////////////")

# 4. Capitales de Europa ordenadas alfabéticamente junto con el país
paises = session.query(Pais).filter(Pais.continente == 'EU').order_by(Pais.capital).all()
for p in paises:
    print(p.capital, "-", p.nombre_pais)

print("/////////////////////////////////////////////////////////////////////////////////////")

# 5. Países cuyo nombre contiene 'uador' o cuya capital termina en 'ito'
paises = session.query(Pais).filter(
    or_(
        Pais.nombre_pais.like('%uador%'),
        Pais.capital.like('%ito%')
    )
).all()
for p in paises:
    print(p.nombre_pais, "-", p.capital)
