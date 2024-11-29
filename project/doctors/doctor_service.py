from database.models import Doctor, session

def add_doctor(name, specialty):
    doctor = Doctor(name=name, specialty=specialty)
    session.add(doctor)
    session.commit()
    return doctor.id
