import datetime

from sqlalchemy import Boolean, Column, DateTime, \
    ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

from app.database import Base

episode_character_table = Table(
    'episode_character', Base.metadata,
    Column('episode_id', ForeignKey('episodes.id'), primary_key=True),
    Column('character_id', ForeignKey('characters.id'), primary_key=True)
)


class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    air_date = Column(String)
    reference = Column(String)
    characters = relationship(
        "Character",
        secondary=episode_character_table,
        back_populates="episodes")
    comments = relationship("Comment", back_populates="episode")


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    species = Column(String)
    type = Column(String)
    gender = Column(String)
    episodes = relationship(
        "Episode",
        secondary=episode_character_table,
        back_populates="characters")
    comments = relationship("Comment", back_populates="character")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    comments = relationship("Comment", back_populates="user")


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)
    message = Column(Text)

    episode_id = Column(Integer, ForeignKey("episodes.id"))
    episode = relationship("Episode", back_populates="comments")

    character_id = Column(Integer, ForeignKey("characters.id"))
    character = relationship("Character", back_populates="comments")

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="comments")
