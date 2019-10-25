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
    __tablename__ = 'Chips'
    id = Column(String,Sequence('chip_id'), primary_key=True)
    code = Column(String(12))
    code_from_user = Column(Integer,ForeignKey('users.id'))
    code_from   = relationship(User, foreign_keys=[code_from_user])
