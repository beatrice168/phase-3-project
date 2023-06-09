import click
from sqlalchemy.orm import sessionmaker
from models import Parent,Student
from sqlalchemy import (create_engine)

engine = create_engine("sqlite:///school.db")
Session = sessionmaker(bind=engine)
session = Session()


     
@click.command()
def add_student():
    # session=Session()
    first_name= input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    grade_in=input("Enter your grade: ")
    position_in=input("Enter your position: ")
    parent_id=input("Enter the parent id: ")
    teacher_id=input("Enter the teacher id: ")
    student=Student(first_name=first_name,last_name=last_name,grade_in=grade_in,position_in=position_in,parent_id=parent_id,teacher_id=teacher_id)
    session.add(student)
    session.commit()
    # session.close()
    print(f'added student {first_name} {last_name} ')

@click.command()
def add_parent():
    # session=Session()
    first_name=input("Enter your first name: ")
    last_name=input("Enter your last name: ")
    age=input("Enter your age: ")
    parent=Parent(first_name=first_name,last_name=last_name,age=age)
    session.add(parent)
    session.commit()
    #session.close()
    print(f'Added parent {first_name} {last_name}')
    
if __name__=='__main__':
    Session=sessionmaker(bind=engine)

    while True:
        print("\nSchool management system")
        print("1. Add Student")
        print("2. Add Parent")
        print("3. Quit")

        choice=input("Enter your choice (1-3)")
        if choice == '1':
            add_student()
        elif choice =='2':
            add_parent()
        elif choice=='3':
            break
        else:
            print("Invalid choice.opppsy! Try again.")
