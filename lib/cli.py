import click
from sqlalchemy.orm import sessionmaker
from models import Parent,Student,Teacher
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    pass
@cli.command()
def create_db():
    engine = create_engine('sqlite:///school.db', echo=True)
    Base.metadata.create_all(engine)
    print("Database created successfully.")

@cli.command()
@click.option('--first-name', prompt='Enter the first name')
@click.option('--last-name', prompt='Enter the last name')
def add_teacher(first_name, last_name):
    teacher = Teacher(first_name=first_name, last_name=last_name)
    session.add(teacher)
    session.commit()
    print("Teacher added successfully.")

@cli.command()
@click.option('--first-name',prompt='Enter the firstname')
@click.option('--last-name',prompt='Enter the lastname')
@click.option('--grade_in',prompt='Enter grade in')
@click.option('--age_in',prompt='Enter age in')
def add_student(first_name,last_name,grade_in,age_in):
    student=Student(first_name=first_name,last_name=last_name,grade_in=grade_in,age_in=age_in)
    session.add(student)
    session.commit()
    print("Student added successfully ")

@cli.command()
@click.option('--first-name',prompt='Enter the firstname')
@click.option('--last-name',prompt='Enter the lastname')
@click.option('--age',prompt='Enter your age')
def add_parent(first_name,last_name,age):
    parent=Parent(first_name=first_name,last_name=last_name,age=age)
    session.add(parent)
    session.commit()
    print("Parent is added successfully")
cli.add_command(add_teacher)  # Register the add_teacher command
cli.add_command(add_student)
cli.add_command(add_parent)


if __name__ == '__main__':
    cli()





