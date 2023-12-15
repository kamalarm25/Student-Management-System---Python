""""
Group Project
Student Class
Author: Kamala Ramesh (700745451)
"""

import sqlalchemy
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select,delete, update, desc

# Create a base class for declarative models
base = declarative_base()
meta = base.metadata

class Student(base):
    __tablename__ = 'student'
    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    age = Column(Integer)
    gender = Column(String(1))
    major = Column(String(32))
    phone = Column(String(32))

    def __init__(self, id, name, age, gender, major, phone):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.major = major
        self.phone = phone

    def __str__(self):
        return (f'id: {self.id}, name: {self.name}, age: {self.age}, gender: {self.gender}, '
                f'major: {self.major}, phone: {self.phone}')

    def __repr__(self):
        return (f'Student ({self.id!r},{self.name!r},{self.age!r},{self.gender!r},'
                f'{self.major!r},{self.phone!r})')

def create_db():
    engine = sqlalchemy.create_engine('sqlite:///user.db')
    #meta.create_all(engine) # run only once to create db
    return engine

def init_db():
    #s1 = Student(id = '700300001', name='Joe Biden', age = 21, gender = 'M', major = 'CS', phone = '816-111-1111')
    #s2 = Student(id = '700300002', name='Donald Trump', age = 23, gender = 'M', major = 'CYBR', phone = '816-402-1111')
    #session.add(s2)
    #session.execute(delete(Student).where(Student.id == 700300001))
    #session.commit()
    pass

session = sessionmaker(bind=create_db())()

if __name__ == '__main__':
    init_db()