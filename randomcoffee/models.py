from os import getenv

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects import postgresql as pg
import sqlalchemy as sa

Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class Coffeeman(Base):
    __tablename__ = "coffeemans"
    id = sa.Column(sa.Integer, primary_key=True)
    chat_id = sa.Column(sa.BigInteger)
    first_name = sa.Column(sa.String)
    last_name = sa.Column(sa.String, nullable=True)
    username = sa.Column(sa.String, nullable=True)
    city = sa.Column(sa.Integer, sa.ForeignKey(City.id))
    interval = sa.Column(sa.Integer)


class Meeting(Base):
    __tablename__ = "meetings"
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime, server_default=sa.func.now(), index=True)


Response = pg.ENUM(
    'ACCEPTED',
    'TIMEOUT',
    'DECLINED',
    name='coffeeman_meetings_response',
)


class CoffeemanMeetings(Base):
    __tablename__ = "coffeeman_meetings"
    coffeeman_id = sa.Column(sa.Integer, sa.ForeignKey(Coffeeman.id),
                             primary_key=True, index=True)
    meeting_id = sa.Column(sa.Integer, sa.ForeignKey(Meeting.id),
                           primary_key=True, index=True)
    response = sa.Column(Response)


db = scoped_session(sessionmaker(bind=sa.create_engine(
    getenv('RANDOMCOFFEE_DB', 'postgresql:///randomcoffee')
)))
