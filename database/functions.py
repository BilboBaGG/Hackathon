from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, MetaData
import time
from models.user import User

from config.hosts import *

class ORM:
    def __init__(self): # Creating database
        time.sleep(3)
        self.engine = create_engine(DBSTRING)  
        
        self.meta = MetaData(self.engine)  

        self.userTable = Table('users', self.meta, 
                       Column('username', String),
                       Column('password', String)) # Create table class

        self.marketTable = Table('markets', self.meta, 
                       Column('name', String),
                       Column('code', String)) # Create table class
        
        self.pointsTable = Table('points', self.meta, 
                       Column('name', String),
                       Column('market_code', String),
                       Column('code', String)) # Create table class

        self.agentTable = Table('agents', self.meta, 
                       Column('name', String),
                       Column('point_code', String)) # Create table class

        self.meta.create_all(self.engine)

        session = self.getSession()

        session.add(Student(username="admin", password="HELLO_WORLD"))
        session.commit()

        print(session.scalars(select(User).filter_by(username="admin")).first().password)

        
    def getSession(self):
        Session = sessionmaker(self.engine)
        return Session()