from typing import Optional
from sqlalchemy import Integer, Column, String, Enum, DateTime, ForeignKey, BigInteger, Boolean
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class UserRole(PyEnum):
    User = "User"
    Worker = "Worker"
    Admin = "Admin"

class ReservationStatus(PyEnum):
    Reserved = "Reserved"
    Awaiting = "Awaiting"
    Cancelled = "Cancelled"
    PastDue = "PastDue"
    Succeeded = "Succeeded"

class UserInfo(Base):
    __tablename__ = "user_infos"

    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String(20), nullable=True)
    card_num = Column(String, nullable=False)

class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True, autoincrement=True)
        email = Column(String, nullable=False, unique=True)
        password = Column(String, nullable=False)
        user_infos_id = Column(Integer, ForeignKey("user_infos.id"), nullable=False)
        role = Column(Enum(UserRole), nullable=False)
        created_at = Column(DateTime, default=datetime.now(), nullable=False)

        user_info = relationship("UserInfo", backref="users")

class Person(Base):
    __tablename__ = "persons"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    birth_year = Column(Optional[Integer], nullable=True)
    death_year = Column(Optional[Integer], nullable=True)

class Language(Base):
    __tablename__ = "languages"
    id= Column(Integer, primary_key=True, autoincrement=True)
    lang = Column(String, nullable=False, unique=True)

class Publisher(Base):
    __tablename__ = "publishers"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    localization = Column(String, nullable=False)
    foundation_year = Column(Integer, nullable=False)

class BookCategory(Base):
    __tablename__ = "book_categories"
    #id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)
    category_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    category = relationship("Category")

class Category(Base):
    __tablename__ = "categories"
    id= Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False, unique=True)

class Form(Base):
    __tablename__ = "forms"
    id= Column(Integer, primary_key=True, autoincrement=True)
    form = Column(String, nullable=False, unique=True)

class Book(Base):
    __tablename__ = "books"
    id= Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    lang_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    series = Column(Optional[String], nullable=True)
    author_id = Column(Integer, ForeignKey("persons.id"), nullable=False)

    lang = relationship("Language", backref="books")
    author = relationship("Person", backref="books")
    categories = relationship("BookCategory")
    annotations = relationship("Annotation", back_populates="book")

class EditionInfo(Base):
    __tablename__ = "edition_infos"
    id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    ed_title = Column(String, nullable=False)
    ed_series = Column(Optional[String], nullable=True)
    illustrator_id = Column(Optional[Integer], ForeignKey("persons.id"), nullable=True)
    translator_id = Column(Optional[Integer], ForeignKey("persons.id"), nullable=True)
    ed_lang_id = Column(Optional[Integer], ForeignKey("languages.id"), nullable=True)
    publisher_id = Column(Integer, ForeignKey("publishers.id"), nullable=False)
    ed_num = Column(Integer, nullable=False)
    ed_year = Column(Integer, nullable=False)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    isbn = Column(BigInteger, nullable=False)
    ukd = Column(String, nullable=False)

    book = relationship("Book")
    illustrator = relationship("Person")
    translator = relationship("Person")
    ed_lang = relationship("Language")
    publisher = relationship("Publisher")
    form = relationship("Form")
    annotations = relationship("Annotation", back_populates="edition")

class Copy(Base):
    __tablename__ = "copies"
    id= Column(Integer, primary_key=True, autoincrement=True)
    ed_id = Column(Integer, ForeignKey("edition_infos.id"), nullable=False)
    rented = Column(Boolean, nullable=False)

    edition = relationship("EditionInfo")
    annotations = relationship("Annotation", back_populates="copy")

class Rental(Base):
    __tablename__ = "rentals"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id"), nullable=False)
    rental_date = Column(DateTime, nullable=False)
    due_date = Column(DateTime, nullable=False)
    return_date = Column(Optional[DateTime], nullable=True)

    user = relationship("User")
    copy = relationship("Copy")

class Annotation(Base):
    __tablename__ = "annotations"
    id= Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Optional[Integer], ForeignKey("books.id"), nullable=True)
    ed_id = Column(Optional[Integer], ForeignKey("edition_infos.id"), nullable=True)
    copy_id = Column(Optional[Integer], ForeignKey("copies.id"), nullable=True)
    content = Column(String, nullable=False)

    book = relationship(Optional["Book"], back_populates="annotations")
    edition = relationship(Optional["EditionInfo"], back_populates="annotations")
    copy = relationship(Optional["Copy"], back_populates="annotations")

class Reservation(Base):
    __tablename__ = "reservations"
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    copy_id = Column(Integer, ForeignKey("copies.id"), nullable=False)
    reserved_at = Column(DateTime, nullable=False)
    reserved_due = Column(DateTime, nullable=False)
    status = Column(Enum(ReservationStatus), nullable=False)

    user = relationship("User")
    copy = relationship("Copy")