#!/usr/bin/python3
'''
    This module defines the BaseModel class
'''
import os
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime


Base = declarative_base()


class BaseModel:
    '''
        Base class
    '''
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    time_stamp = Column(DateTime, default=datetime.utcnow(), nullable=False)
  