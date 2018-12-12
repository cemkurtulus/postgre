from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://localhost:5432/postgres?user=postgres&password=Bjk165165!*')
Session = sessionmaker(bind=engine)

Base = declarative_base()