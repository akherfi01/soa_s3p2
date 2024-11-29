from database.models import MedicalRecord

def create_record(patient_name, details):
    record = MedicalRecord(patient_name=patient_name, details=details)
    session.add(record)
    session.commit()
    return record.id

