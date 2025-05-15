from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_base import Pais

engine = create_engine('sqlite:///basepais.db')
Session = sessionmaker(bind=engine)
session = Session()

# 1.
paises = session.query(Pais).filter(Pais.continente == 'NA').all() 
for p in paises:
    print(p.nombre_pais, "-", p.continente)
    
print("/////////////////////////////////////////////////////////////////////////////////////")

# 2.
paises = session.query(Pais).filter(Pais.continente == 'AS').order_by(Pais.dial).all()
for p in paises:
    print(p.nombre_pais, "-", p.dial)

print("/////////////////////////////////////////////////////////////////////////////////////")

# 3.
# ...

print("/////////////////////////////////////////////////////////////////////////////////////")

# 4.
# ...

print("/////////////////////////////////////////////////////////////////////////////////////")

# 5.
# ...