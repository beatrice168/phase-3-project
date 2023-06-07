import random
import ipdb;
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__=='__main__':
    engine = create_engine('sqlite:///school.db')
    session = sessionmaker(bind=engine)
    session=session()

    ipdb.set_trace()
