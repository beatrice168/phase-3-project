# import os 
# import sys

# sys.path.append (os.getcwd)

from sqlalchemy import (create_engine,Column,Integer,String,ForeignKey,Table)
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///school.db', echo=True)
    session=sessionmaker(bind=engine)
    session=session()

class Teacher(Base):
    __tablename__='teachers'
    id = Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    

    def __repr__(self):
        return f'Teacher: {self.first_name}'
    
class Parent(Base):
    __tablename__='parents'
    id= Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())


    def __repr__(self):
        return f'Parent: {self.first_name}'
    
class Student(Base):
    __tablename__='students'
    id = Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    class_in= Column(Integer())
    age_in=Column(Integer())





