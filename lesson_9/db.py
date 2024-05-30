from sqlalchemy import create_engine, Column, Integer, String, Boolean, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"
    
    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True, nullable=False)
    create_timestamp = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    change_timestamp = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    middle_name = Column(String(20))
    phone = Column(String(15), nullable=False)
    email = Column(String(256))
    avatar_url = Column(String(1024))
    company_id = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)
