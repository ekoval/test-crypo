from sqlalchemy import Column, Integer, JSON, String

from .database import Base


class Portfolio(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    data = Column(JSON, default={})
