from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import connector


class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('app_user_id_seq'), primary_key=True)
    fullname = Column(String(80))
    email = Column(String(80))
    password = Column(String(80))
    balance = Column(String(12))
    

class Chips(connector.Manager.Base):
    __tablename__ = 'chips'
    id = Column(Integer,Sequence('app_chip_id_seq'), primary_key=True)
    code = Column(String(12))
    
    code_from_user = Column(String,ForeignKey('users.id'))

