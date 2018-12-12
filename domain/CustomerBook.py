from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship

from domain.Base import Base


class CustomerBook(Base):
    __tablename__ = "customerbook"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", uselist=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name