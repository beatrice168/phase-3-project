import random
from models import Teacher,Parent,Student,teacher_parent
import ipdb;
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker



if __name__=='__main__':
    engine = create_engine('sqlite:///school.db')
    session = sessionmaker(bind=engine)
    session=session()
    fake=Faker()

    ipdb.set_trace()
