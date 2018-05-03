""" emails model for sqlalchemy """

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
import json


class Email(BaseModel, Base):
    '''
        defines an id to email database for newsletter
    '''
    __tablename__ = "emails"
    email = Column(String(254), nullable=False)

    def __str__(self):
        return  "{}: [ {} ] / \"{}\"".format(self.id, self.email, self.time_stamp)
