from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restu.db')
Session = sessionmaker(bind=engine)
session = Session()