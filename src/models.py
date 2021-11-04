import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    FavCharacter = relationship('favCharacter', backref='user')
    FavPlanet = relationship('favPlanet', backref='user')

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(Integer, nullable=True)
    terrain = Column(String(50), nullable=True)
    favPlanets = relationship('favPlanet', backref='planet', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=True)
    haircolor = Column(String(50), nullable=True)
    eyescolor = Column(String(50), nullable=True)
    favCharacters = relationship('favCharacter', backref='character')

class FavCharacter(Base):
    __tablename__ = 'favcharacter'
    id = Column(Integer, primary_key=True)
    idUser = Column(Integer, ForeignKey('user.id'))
    idCharacter = Column(Integer, ForeignKey('character.id'))

class FavPlanet(Base):
    __tablename__ = 'favplanet'
    id = Column(Integer, primary_key=True)
    idUser = Column(Integer, ForeignKey('user.id'))
    idPlanet = Column(Integer, ForeignKey('planet.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')