from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
   __tablename__ = 'users'
   
   id = Column(String, primary_key=True)
   group = Column(String)