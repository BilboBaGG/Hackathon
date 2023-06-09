from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin

Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   id = Column(String, primary_key=True)
   email = Column(String, primary_key=True)
   username = Column(String)
   password = Column(String)
   is_admin = Column(Boolean)
