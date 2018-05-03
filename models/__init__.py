'''
    Package initializer
'''

from models.engine import DBStorage
from models.base_model import Base
from models.searches import Search
from models.emails import Email


# creating db session
storage = DBStorage()
# creating db file and table if not alredy created
storage.reload()
