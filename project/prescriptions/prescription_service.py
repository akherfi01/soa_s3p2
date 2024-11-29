from database.models import Prescription, session

def add_prescription(patient_id, medication, dosage):
    prescription = Prescription(patient_id=patient_id, medication=medication, dosage=dosage)
    session.add(prescription)
    session.commit()
    return prescription.id
