""""
Group Project
User Registration Class
Author: Kamala Ramesh (700745451)
"""

import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select,delete, update, desc

# Create a base class for declarative models
base = declarative_base()
meta = base.metadata

# Class representing the User table
class User(base):
    __tablename__ = 'user'
    userid = Column(String(32), primary_key=True, nullable=False)
    password = Column(String(512), nullable=False)

    def __init__(self, userid, password):
        self.userid = userid
        self.password = password

    def __str__(self):
        return f'user id: {self.userid}, password: {self.password}'

    def __repr__(self):
        return f'User ({self.userid!r},{self.password!r})'

def create_db():
    engine = sqlalchemy.create_engine('sqlite:///user.db')
    #meta.create_all(engine) # run only once to create db
    return engine

def init_db():
    #u1 = User(userid='Kamala',password='!password1')
    #session.add(u1)
    #session.commit()
    #session.execute(delete(User).where(User.userid == 'Ramesh'))
    #session.commit()
    pass

session = sessionmaker(bind=create_db())()

if __name__ == '__main__':
    init_db()