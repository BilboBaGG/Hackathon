from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   email = Column(String, primary_key=True)
   username = Column(String)
   password = Column(String)