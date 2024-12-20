from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///clinic.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    details = Column(Text, nullable=True)

class Prescription(Base):
    __tablename__ = 'prescriptions'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, nullable=False)
    medication = Column(String, nullable=False)

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    email = Column(String, nullable=False)  
    date = Column(String, nullable=False)
    time = Column(String, nullable=False)
    reason = Column(Text, nullable=False)
    doctor_id = Column(Integer, nullable=False) 




Base.metadata.create_all(engine)
