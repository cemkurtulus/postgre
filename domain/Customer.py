from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from domain.Base import Base

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    books = relationship("CustomerBook", back_populates="customer")

    def __init__(self, id, name, books):
        self.id = id
        self.name = name
        self.books = books