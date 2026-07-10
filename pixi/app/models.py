from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, Float
from sqlalchemy.sql import func
from .db import Base




class Admin(Base):
__tablename__ = 'admins'


id = Column(Integer, primary_key=True)
username = Column(String(150), unique=True, nullable=False)
password_hash = Column(String(255), nullable=False)
is_active = Column(Boolean, default=True)
created_at = Column(DateTime(timezone=True), server_default=func.now())




class Product(Base):
__tablename__ = 'products'


id = Column(Integer, primary_key=True)
name = Column(String(255), nullable=False)
description = Column(Text, nullable=True)
price = Column(Float, nullable=False)
in_stock = Column(Boolean, default=True)
created_at = Column(DateTime(timezone=True), server_default=func.now())
updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())