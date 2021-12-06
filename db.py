from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///got.sqlite')
Session = sessionmaker(bind=engine,autoflush=False)
session = Session()
Base = declarative_base()