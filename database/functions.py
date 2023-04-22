from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, MetaData
import time
from models.user import User
from models.market import Market
from models.point import Point
from models.agent import Agent

from config.hosts import *

class ORM:
    def __init__(self): 
        time.sleep(3)

        # Creating database if not exist
        self.engine = create_engine(DBSTRING)  
        
        self.meta = MetaData(self.engine)  

        self.userTable = Table('users', self.meta, 
                       Column('username', String),
                       Column('password', String),
                       Column('token',String)) # Users table

        self.marketTable = Table('markets', self.meta, 
                       Column('name', String),
                       Column('code', String)) # Markets table
        
        self.pointsTable = Table('points', self.meta, 
                       Column('name', String),
                       Column('market_code', String),
                       Column('point_code', String)) # Points table

        self.agentTable = Table('agents', self.meta, 
                       Column('name', String),
                       Column('point_code', String)) # Agents table

        self.meta.create_all(self.engine)

        if not self.IsUserExists("admin"):
            self.AddUser("admin","secret_password","ALLWAYSHERE")


        if not self.IsPointExists("Baza"):
            self.AddPoint("Baza","AJSDJJSDJ","HELLO")
            print("ha")

        print(self.GetPointByName("Baza").point_code)
        self.UpdatePointsSelfCode("Baza","hahahhaha")
        print(self.GetPointByName("Baza").point_code)



        print(self.GetPointByName("Baza").market_code)
        self.UpdatePointsMarketCode("Basa","lallala")
        print(self.GetPointByName("Baza").market_code)

        print(self.IsPointExists("Baza"))
        self.DeletePoint("Baza")
        print(self.IsPointExists("Baza"))
        


        print(self.GetAllPoints())


    def UpdateSession(self):
        self.engine = create_engine(DBSTRING) 

    def GetSession(self):
        Session = sessionmaker(self.engine)
        return Session()

    # User functions
    def AddUser(self, username_, password_, token_="NULL"):
        session = self.GetSession()
        session.add(User(username=username_, password=password_,token=token_))
        session.commit()

    def GetUserByUsername(self, username_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(username=username_)).first()

    def IsUserExists(self, username_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(username=username_)).first() is not None

    def UpdateUserPassword(self, username_, password_):
        session = self.GetSession()
        session.query(User).filter(User.username==username_).update({'password': password_})
        session.commit()

    def UpdateUserToken(self, username_, token_):
        session = self.GetSession()
        session.query(User).filter(User.username==username_).update({'token': token_})
        session.commit()

    def GetAllUsers(self):
        session = self.GetSession()
        return session.scalars(select(User)).all()

    def DeleteUser(self,username_):
        session = self.GetSession()
        session.query(User).filter(User.username==username_).delete()
        session.commit()

    # Market functions
    def AddMarket(self,name_,code_):
        session = self.GetSession()
        session.add(Market(name=name_, code=code_))
        session.commit()

    def GetMarketByName(self, name_):
        session = self.GetSession()
        return session.scalars(select(Market).filter_by(name=name_)).first()

    def IsMarketExists(self, name_):
        session = self.GetSession()
        return session.scalars(select(Market).filter_by(name=name_)).first() is not None

    def UpdateMarketCode(self, name_, code_):
        session = self.GetSession()
        session.query(Market).filter(Market.name==name_).update({'code': code_})
        session.commit()

    def GetAllMarkets(self):
        session = self.GetSession()
        return session.scalars(select(Market)).all()

    def DeleteMarket(self,name_):
        session = self.GetSession()
        session.query(Market).filter(Market.name==name_).delete()
        session.commit()

    # Point functions
    def AddPoint(self, name_, point_code_, market_code_="NULL"):
        session = self.GetSession()
        session.add(Point(name=name_, point_code=point_code_, market_code=market_code_))
        session.commit()

    def GetPointByName(self, name_):
        session = self.GetSession()
        return session.scalars(select(Point).filter_by(name=name_)).first()

    def IsPointExists(self, name_):
        session = self.GetSession()
        return session.scalars(select(Point).filter_by(name=name_)).first() is not None

    def UpdatePointsSelfCode(self, name_, point_code_):
        session = self.GetSession()
        session.query(Point).filter(Point.name==name_).update({'point_code': point_code_})
        session.commit()

    def UpdatePointsMarketCode(self, name_, market_code_):
        session = self.GetSession()
        session.query(Point).filter(Point.name==name_).update({'market_code': market_code_})
        session.commit()

    def GetAllPoints(self):
        session = self.GetSession()
        return session.scalars(select(Point)).all()

    def DeletePoint(self,name_):
        session = self.GetSession()
        session.query(Point).filter(Point.name==name_).delete()
        session.commit()
