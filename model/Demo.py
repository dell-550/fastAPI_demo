from sqlalchemy import Column, String, Integer
from .db import Base


class DemoModel(Base):
    __tablename__ = 'demo'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    number = Column(String(20))
    password = Column(String(200))
