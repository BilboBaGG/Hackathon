from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Point(Base):
   __tablename__ = 'points'
   
   name = Column(String, primary_key=True)
   point_code = Column(String)
   market_code = Column(String)