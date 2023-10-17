from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core import settings

"""
This module is responsible for creating the SQLAlchemy engine and session.
"""

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
