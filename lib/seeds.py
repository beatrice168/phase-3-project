from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from models import Teacher, Parent, Student,teacher_parent

if __name__=='__main__':
    engine = create_engine('sqlite:///school.db')
    session = sessionmaker(bind=engine)
    session=session()
    session.query(teacher_parent).delete()
    session.query(Student).delete()
    session.query(Teacher).delete()
    session.query(Parent).delete()    
    fake=Faker()

    teachers=[]
    for _ in range (20):
        teacher=Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )
        session.add(teacher)
        teachers.append(teacher)
    parents=[]
    for _ in range(20):
        parent=Parent(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            age=random.randint(30, 50)
        )
        session.add(parent)
        parents.append(parent)

    existing_combinations=set()
    for _ in range (50):
        teacher_id=random.randint(1,20)
        parent_id= random.randint(1,20)
        
        if (teacher_id, parent_id)in existing_combinations:
            continue
        existing_combinations.add((teacher_id,parent_id))
        teacher_parent_data={"teacher_id":teacher_id, "parent_id":parent_id}
        stmt= insert(teacher_parent).values(teacher_parent_data)
        session.execute(stmt)

    for _ in range(50):
        student=Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            grade_in=random.randint(9,12),
            age_in=random.randint(12,18),
            position_in=random.randint(1, 50),
            parent_id=random.randint(1,20),
            teacher_id=random.randint(1,20)
        )
        session.add(student)

    session.commit()
    session.close()

    
        
