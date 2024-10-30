from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base

#Base = declarative_base()

class Rental(Base):
    __tablename__ = 'rentals'
    id =          Column(Integer, primary_key=True,        nullable=False, index=True)
    user_id =     Column(Integer, ForeignKey('users.id'),  nullable=False)
    copy_id =     Column(Integer, ForeignKey('copies.id'), nullable=False)
    rental_date = Column(Date,                             nullable=False)
    due_date =    Column(Date,                             nullable=False)
    return_date = Column(Date,                             nullable=True)


class Category(Base):
    __tablename__ = 'categories'
    id =       Column(Integer, primary_key=True, nullable=False, index=True)
    category = Column(String, unique=True,       nullable=False)


class Book(Base):
    __tablename__ = 'books'
    id =        Column(Integer, primary_key=True,           nullable=False, index=True)
    title =     Column(String,                              nullable=False)
    series =    Column(String,                              nullable=True)
    lang_id =   Column(Integer, ForeignKey('languages.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('persons.id'),   nullable=False)


class Person(Base):
    __tablename__ = 'persons'
    id =         Column(Integer, primary_key=True, nullable=False, index=True)
    name =       Column(String,                    nullable=False)
    surname =    Column(String,                    nullable=True) # e.g. Herodot
    birth_year = Column(Integer,                   nullable=True)
    death_year = Column(Integer,                   nullable=True)


class Language(Base):
    __tablename__ = 'languages'
    id =   Column(Integer, primary_key=True, nullable=False, index=True)
    lang = Column(String, unique=True,       nullable=False)


class Publisher(Base):
    __tablename__ = 'publishers'
    id =              Column(Integer, primary_key=True, nullable=False, index=True)
    name =            Column(String,                    nullable=False)
    city =            Column(String,                    nullable=False)
    foundation_year = Column(Integer,                   nullable=False)


class EditionInfo(Base):
    __tablename__ = 'edition_infos'
    id =             Column(Integer, primary_key=True, index=True,nullable=False)
    book_id =        Column(Integer, ForeignKey('books.id'),      nullable=False)
    ed_title =       Column(String,                               nullable=True)
    ed_series =      Column(String,                               nullable=True)
    ed_lang_id =     Column(Integer, ForeignKey('languages.id'),  nullable=True)
    ed_num =         Column(Integer,                              nullable=False)
    ed_year =        Column(Integer,                              nullable=False)
    illustrator_id = Column(Integer, ForeignKey('persons.id'),    nullable=True)
    translator_id =  Column(Integer, ForeignKey('persons.id'),    nullable=True)
    publisher_id =   Column(Integer, ForeignKey('publishers.id'), nullable=False)
    form =           Column(Integer,                              nullable=False)
    isbn =           Column(Integer,                              nullable=False)
    ukd =            Column(String,                               nullable=False)


class Copy(Base):
    __tablename__ = 'copies'
    id =     Column(Integer, primary_key=True, index=True,   nullable=False)
    ed_id =  Column(Integer, ForeignKey('edition_infos.id'), nullable=False)
    rented = Column(Boolean,                                 nullable=False)


class Annotation(Base):
    __tablename__ = 'annotations'
    id =      Column(Integer, primary_key=True, index=True,   nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'),         nullable=True)
    ed_id =   Column(Integer, ForeignKey('edition_infos.id'), nullable=True)
    copy_id = Column(Integer, ForeignKey('copies.id'),        nullable=True)
    content = Column(String,                                  nullable=False)


class BookToCategory(Base):
    __tablename__ = 'books_to_categories'
    book_id =     Column(Integer, ForeignKey('books.id'),      primary_key=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True, nullable=False)