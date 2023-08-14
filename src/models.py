import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name=Column(String(50), nullable=False)
    email= Column(String(50), nullable=False)
    password= Column(String(20), nullable=False)
    date_sus=Column(String(20),nullable=False)
    favorites= relationship("Favorities", backref="user")


class Planet(Base):
    __tablename__='planet'
    id=Column(Integer, primary_key=True)
    name= Column(String(50),nullable=True)
    population= Column(Integer, nullable=True)
    rotation_period= Column(Integer,nullable=False)
    orbital_period= Column(Integer,nullable=False)
    diameter= Column(Integer,nullable=False)
    climate= Column(String(50),nullable=False)
    gravity= Column(String(50),nullable=False)
    terrain= Column(String(50),nullable=False)
    surface_water= Column(Integer,nullable=False)
    people_id= relationship("People", backref="planet")
    favorities= relationship("Favorities", backref="planet")



class People(Base):
    __tablename__='people'
    id=Column(Integer, primary_key=True)
    name= Column(String(50),nullable=False)
    height= Column(Integer,nullable=False)
    mass= Column(Integer,nullable=True)
    hair_color= Column(String(50),nullable=True)
    skin_color= Column(String(50),nullable=True)
    eye_color= Column(String(50),nullable=False)
    birth_year= Column(String(50),nullable=False)
    gender= Column(String(50),nullable=False)
    planet_id= Column(Integer, ForeignKey("planet.id"), nullable=True)
    favorities= relationship("Favorites", backref="poeple")
  
    
class Favorites(Base):
    __tablename__='favorities'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey("user.id"), nullable=False)
    planet_id= Column(Integer,ForeignKey("planet.id"), nullable=True)
    people_id= Column(Integer, ForeignKey("people.id"),nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
