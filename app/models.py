from sqlalchemy import Column, ForeignKey, Integer, String
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
