
from sqlalchemy import (create_engine,Column,Integer,String,ForeignKey,Table)
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///school.db', echo=True)
    session=sessionmaker(bind=engine)
    session=session()

teacher_parent= Table(
    "teacher_parent",
    Base.metadata,
    Column("teacher_id", ForeignKey("teachers.id"),primary_key=True),
    Column("parent_id", ForeignKey("parents.id"),primary_key=True),
    extend_existing=True,
)

class Teacher(Base):
    __tablename__='teachers'
    id = Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    students=relationship('Student',backref=backref("teacher"))
    parents=relationship("Parent", secondary="teacher_parent",back_populates="teachers")

    def __repr__(self):
        return f'Teacher: {self.first_name}'
    def teacher_pupils(self):
        return self.students
    def teacher_wazazi(self):
        return self.parents
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def fav_student(self):
        fav_student=session.query(Student).order_by(Student.position_in.desc()).first()
        return fav_student
    # def add_student(self):
    #     student=Student(teacher= self, )
    # def eliminate_student(self):
    #     students_to_eliminate=[student for student in self.students if student.]
class Parent(Base):
    __tablename__='parents'
    id= Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    age=Column(Integer())
    students=relationship("Student",backref=backref("parent"))
    teachers=relationship("Teacher",secondary="teacher_parent",back_populates="parents")


    def __repr__(self):
        return f'Parent: {self.first_name}'
    def student(self):
        return self.students
    def teacher(self):
        return self.teachers
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    @classmethod
    def oldest_parent(cls,session):
        return session.query(cls).order_by(cls.age.desc()).first()
    
    # def all_students(self):
    #     return f'Parent of {self.student}'
    
class Student(Base):
    __tablename__='students'
    id = Column(Integer(), primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    grade_in= Column(Integer())
    age_in=Column(Integer())
    position_in=Column(Integer())
    parent_id=Column(Integer(), ForeignKey("parents.id"))
    teacher_id=Column(Integer(),ForeignKey("teachers.id"))
    def parent(self):
        return self.parent
    def teacher(self):
        return self.teacher
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    def __repr__(self):
        return f'Student(id={self.id}),'+ \
            f'first_name={self.first_name},'+ \
            f'last_name = {self.last_name},'+ \
            f'class_in={self.class_in},'+ \
            f'age_in={self.age_in},'+ \
            f'position_in={self.position_in},'+ \
            f'parent_id={self.parent_id},'+ \
            f'teacher_id={self.teacher_id},'
            




