from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, String, MetaData, Integer, Boolean
import time, hashlib
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
                        Column('id',String),
                        Column('email',String),
                        Column('username', String),
                        Column('password', String),
                        Column('is_admin', Boolean)) # Users table

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

        if not self.IsUserExists(hashlib.sha256(b'admin').hexdigest()):
            self.AddUser(email_="admin@erratas.htb",username_="admin",password_=hashlib.sha256(b"secret_password").hexdigest(),is_admin_=True)

        print(self.CheckUser("admin",hashlib.sha256(b"secret_password").hexdigest()))

    def UpdateSession(self):
        self.engine = create_engine(DBSTRING) 

    def CheckUser(self,username_,passwordhash_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(username=username_, password=passwordhash_)).first() is not None


    def GetSession(self):
        Session = sessionmaker(self.engine)
        return Session()

    # User functions
    def AddUser(self, email_, username_, password_, is_admin_=False):
        session = self.GetSession()
        session.add(User(id=hashlib.sha256(username_.encode()).hexdigest(),email=email_,username=username_, password=password_, is_admin=is_admin_))
        session.commit()

    def GetUserByUsername(self, username_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(username=username_)).first()

    def IsAdmin(self, username_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(username=username_)).first().is_admin

    def GetUserByEmail(self,email_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(email=email_)).first()

    def GetUserByID(self,id_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(id=id_)).first()

    def IsUserExists(self, id_):
        session = self.GetSession()
        return session.scalars(select(User).filter_by(id=id_)).first() is not None

    def UpdateUserPassword(self, id_, password_):
        session = self.GetSession()
        session.query(User).filter(User.id==id_).update({'password': password_})
        session.commit()

    def UpdateUsername(self, id_, username_):
        session = self.GetSession()
        session.query(User).filter(User.id==id_).update({'username': username_})
        session.commit()

    def UpdateUserEmail(self, id_, email_):
        session = self.GetSession()
        session.query(User).filter(User.id==id_).update({'email': email_})
        session.commit()

    def GetAllUsers(self):
        session = self.GetSession()
        return session.scalars(select(User)).all()

    def DeleteUser(self, id_):
        session = self.GetSession()
        session.query(User).filter(User.id==id_).delete()
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

    # Agent functions
    def AddAgent(self, name_, point_code_):
        session = self.GetSession()
        session.add(Agent(name=name_, point_code=point_code_))
        session.commit()

    def GetAgentByName(self, name_):
        session = self.GetSession()
        return session.scalars(select(Agent).filter_by(name=name_)).first()

    def IsAgentExists(self, name_):
        session = self.GetSession()
        return session.scalars(select(Agent).filter_by(name=name_)).first() is not None

    def UpdateAgentPointCode(self, name_, point_code_):
        session = self.GetSession()
        session.query(Agent).filter(Agent.name==name_).update({'point_code': point_code_})
        session.commit()

    def GetAllAgents(self):
        session = self.GetSession()
        return session.scalars(select(Agent)).all()

    def DeleteAgent(self,name_):
        session = self.GetSession()
        session.query(Agent).filter(Agent.name==name_).delete()
        session.commit()