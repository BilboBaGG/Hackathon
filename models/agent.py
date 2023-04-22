from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Agent(Base):
   __tablename__ = 'users'
   
   name = Column(String, primary_key=True)
   market_code = Column(String)
   code = Column(String)