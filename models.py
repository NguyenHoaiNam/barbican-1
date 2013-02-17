# -*- coding: utf-8 -*-
"""
    Barbican Models
    ~~~~~~~~~~~~~~~

    The models for Barbican.

    :copyright: (c) 2013 by Jarret Raim
    :license: Apache 2.0, see LICENSE for details
"""
from uuid import uuid4
from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(50))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


class Tenant(Base):
    __tablename__ = 'tenants'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True)

    def __init__(self, uuid=None):
        if uuid is None:
            self.uuid = str(uuid4())

    def __repr__(self):
        return '<Tenant %s>' % self.uuid
