from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr

"""
This module contains the Base class, from which all the ORM models will inherit.
"""

@as_declarative()
class Base:
    """
    Base class for ORM models, providing an auto-generated tablename and an id attribute.
    """
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
