from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Agent(Base):
   __tablename__ = 'agents'
   
   name = Column(String, primary_key=True)
   point_code = Column(String)