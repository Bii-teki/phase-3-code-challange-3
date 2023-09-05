#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import Restaurant, Customer, Review

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///restu.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()
