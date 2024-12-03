from zeep import Client
from faker import Faker
import random

fake = Faker()

# Functions to generate data
def generate_patient():
    return {
        "name": fake.name(),
        "age": random.randint(0, 100),
        "diagnosis": fake.sentence(nb_words=5)
    }

def generate_doctor():
    return {
        "name": fake.name(),
        "specialty": random.choice(["Cardiology", "Neurology", "Pediatrics", "Orthopedics"])
    }

def generate_medical_record(patient_id, doctor_id):
    return {
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "diagnosis": fake.sentence(nb_words=5),
        "prescription": fake.text(max_nb_chars=50)
    }

# SOAP client
wsdl = "http://localhost:5000/soap/?wsdl"  # Replace with your WSDL URL
client = Client(wsdl=wsdl)

# Lists to store created IDs
patient_ids = []
doctor_ids = []

# Create 100 doctors
for _ in range(100):
    doctor_data = generate_doctor()
    response = client.service.add_doctor(**doctor_data)
    print("Doctor Created:", response)
    # Assuming response contains the doctor ID
    doctor_id = int(response.split(":")[-1].strip())
    doctor_ids.append(doctor_id)

# Create 100 patients
for _ in range(100):
    patient_data = generate_patient()
    response = client.service.create_record(**patient_data)
    print("Patient Created:", response)
    # Assuming response contains the patient ID
    patient_id = int(response.split(":")[-1].strip())
    patient_ids.append(patient_id)

# Create 100 medical records
for _ in range(100):
    if not patient_ids or not doctor_ids:
        print("No patients or doctors available to create records.")
        break
    patient_id = random.choice(patient_ids)
    doctor_id = random.choice(doctor_ids)
    medical_record_data = generate_medical_record(patient_id, doctor_id)
    response = client.service.add_prescription(**medical_record_data)
    print("Medical Record Created:", response)

