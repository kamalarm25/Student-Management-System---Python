""""
Group Project
Score Class
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

class Score(base):
    __tablename__ = 'score'
    id = Column(String(9), primary_key=True, unique=True)
    name = Column(String(32), nullable=False)
    CS1030 = Column(Integer)
    CS1100 = Column(Integer)
    CS2030 = Column(Integer)

    def __init__(self, id, name, CS1030, CS1100, CS2030):
        self.id = id
        self.name = name
        self.CS1030 = CS1030
        self.CS1100 = CS1100
        self.CS2030 = CS2030

    def __str__(self):
        return (f'id: {self.id}, name: {self.name}, CS1030: {self.CS1030}, '
                f'CS1100: {self.CS1100}, CS2030: {self.CS2030}')

    def __repr__(self):
        return (f'Student ({self.id!r},{self.name!r},{self.CS1030!r},{self.CS1100!r},{self.CS2030!r})')

def create_db():
    engine = sqlalchemy.create_engine('sqlite:///user.db')
    meta.create_all(engine) # run only once to create db
    return engine

def init_db():
    #o1 = Score(id = '700300001', name='Joe Biden', CS1030=0, CS1100=0, CS2030=0)
    #o2 = Score(id = '700300002', name='Donald Trump', CS1030=0, CS1100=0, CS2030=0)
    #o3 = Score(id = '700300003', name='Donald Trump', CS1030=0, CS1100=0, CS2030=0)
    #o4 = Score(id = '700300004', name='Abraham Lincoln', CS1030=0, CS1100=0, CS2030=0)
    #o5 = Score(id = '700300005', name='Franklin Roosevelt', CS1030=0, CS1100=0, CS2030=0)

    session.execute(delete(Score).where(Score.id == 700300009))
    #session.add_all([o1,o2,o3,o4,o5])
    session.commit()
    pass

session = sessionmaker(bind=create_db())()

if __name__ == '__main__':
    init_db()
