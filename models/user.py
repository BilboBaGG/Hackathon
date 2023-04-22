from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   email = Column(String, primary_key=True)
   username = Column(String)
   password = Column(String)