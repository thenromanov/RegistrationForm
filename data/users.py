import datetime
import sqlalchemy
from sqlalchemy import orm, Integer, String, DateTime, Column
from .dbSession import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String, nullable=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    position = Column(String, nullable=True)
    speciality = Column(String, nullable=True)
    address = Column(String, nullable=True)
    email = Column(String, index=True, unique=True)
    hashedPassword = sqlalchemy.Column(String, nullable=True)
    modifiedDate = sqlalchemy.Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<User> {self.id} {self.name} {self.surname} {self.email}'

    def setPassword(self, password):
        self.hashedPassword = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.hashedPassword, password)
