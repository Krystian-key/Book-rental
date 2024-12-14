
class Publisher(Base):
    __tablename__ = "publishers"
    id= Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    localization = Column(String, nullable=False)
    foundation_year = Column(Integer, nullable=False)
