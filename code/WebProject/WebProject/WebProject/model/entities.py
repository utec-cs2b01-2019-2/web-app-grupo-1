from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from WebProject.database import connector


class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    fullname = Column(String(80))
    email = Column(String(80))
    password = Column(String(80))
    

class Chips(connector.Manager.Base):
    __tablename__ = 'chips'
    id = Column(Integer,Sequence('chip_id_seq'), primary_key=True)
    code = Column(String(12))
    code_from_user = Column(String,ForeignKey('users.id'))

