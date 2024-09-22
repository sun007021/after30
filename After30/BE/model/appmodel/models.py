from sqlalchemy import Column, Integer, String, Date
from core.db import Base


class Users(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    sex = Column(String(1), nullable=False)
    birth = Column(Date, nullable=True)
    phone = Column(String, nullable=False)
