from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgres import JSONB
from sqlalchemy import Column, INTEGER

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True)
    data = Column(JSONB)
