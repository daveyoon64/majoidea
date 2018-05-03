from models import storage, Search, Email
from datetime import datetime


if __name__ == "__main__":
    testEmail = Email()
    setattr(testEmail, "email", "thabest@inthe.world")
    setattr(testEmail, "time_stamp", datetime.utcnow())
    storage.new(testEmail)
    storage.save()
    print(storage.query_object(Email))
