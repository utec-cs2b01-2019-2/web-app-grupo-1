from sqlalchemy import Column, Integer, String, Sequence, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from WebProject.database import connector


class User(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    lastname = Column(String(50))
    password = Column(String(12))
    email = Column(String(40))

class Chip(connector.Manager.Base):
    __tablename__ = 'Chips'
    id = Column(Integer,Sequence('chip_id'), primary_key=True)
    code = Column(Integer(12))
    code_from_user = Column(Integer,ForeignKey('users.id'))
    code_from_user = relationship(User, foreign_key=[code_from_user])
