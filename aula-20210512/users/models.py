from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'tb_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False)
    passwd = Column(String(255), nullable=False)
    level = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow())

    profile = relationship("UserProfile", uselist=False, back_populates="user")


class UserProfile(Base):
    __tablename__ = 'tb_users_profiles'

    id = Column(Integer, ForeignKey('tb_users.id'), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(DateTime, nullable=False)

    user = relationship("User", uselist=False, back_populates="profile")
