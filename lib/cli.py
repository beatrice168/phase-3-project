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
def add_student(first_name,last_name):
    student=Student(first_name=first_name,last_name=last_name)
    session.add(student)
    session.commit()
    print("Student added successfully ")
cli.add_command(add_teacher)  # Register the add_teacher command
cli.add_command(add_student)
# Add more commands as needed


if __name__ == '__main__':
    cli()





