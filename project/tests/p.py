import os
import requests
from zeep import Client, Transport

# Base URLs
REST_BASE_URL = "http://localhost:5000/api"
SOAP_BASE_URL = "http://localhost:5000/soap?wsdl"

# SOAP client setup
soap_client = Client(SOAP_BASE_URL, transport=Transport(timeout=10))


# --- Utility Functions ---
def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Pause to let the user view the output."""
    input("\nPress Enter to continue...")


def handle_rest_response(response):
    """Handles REST responses by checking status codes and returning parsed JSON."""
    try:
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed to parse JSON response: {e}")
    return None


def handle_soap_request(func, *args):
    """Handles SOAP requests and prints the result or error."""
    try:
        result = func(*args)
        print(f"Response: {result}")
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()


# --- APPOINTMENTS FUNCTIONS ---
def create_appointment():
    print("\n--- Create Appointment ---")
    data = {
        "patient_name": input("Enter patient name: "),
        "email": input("Enter patient email: "),
        "date": input("Enter appointment date (YYYY-MM-DD): "),
        "time": input("Enter appointment time (HH:MM): "),
        "reason": input("Enter appointment reason: "),
        "doctor_id": int(input("Enter doctor ID: ")),  # Prompt for doctor ID
    }
    response = requests.post(f"{REST_BASE_URL}/appointments", json=data)
    appointments = handle_rest_response(response)
    if appointments:
        for appointment in appointments:
            print(f"\nAppointment ID: {appointment['id']}")
            print(f"Patient Name: {appointment['patient_name']}")
            print(f"Email: {appointment['email']}")
            print(f"Date: {appointment['date']}")
            print(f"Time: {appointment['time']}")
            print(f"Reason: {appointment['reason']}")
            print("-" * 30)
    pause()


def list_appointments():
    print("\n--- List Appointments ---")
    response = requests.get(f"{REST_BASE_URL}/appointments")
    appointments = handle_rest_response(response)

    if appointments:
        for appointment in appointments:
            print(f"\nAppointment ID: {appointment['id']}")
            print(f"Patient Name: {appointment['patient_name']}")
            print(f"Email: {appointment['email']}")
            print(f"Date: {appointment['date']}")
            print(f"Time: {appointment['time']}")
            print(f"Reason: {appointment['reason']}")
            print("-" * 30)
    else:
        print("No appointments found.")
    pause()


def delete_appointment():
    print("\n--- Delete Appointment ---")
    appointment_id = input("Enter appointment ID: ")
    response = requests.delete(f"{REST_BASE_URL}/appointments/{appointment_id}")
    print(f"Response: {handle_rest_response(response)}")
    pause()


# --- MEDICAL RECORDS FUNCTIONS ---
def create_medical_record():
    print("\n--- Create Medical Record ---")
    handle_soap_request(
        soap_client.service.create_record,
        input("Enter patient name: "),
        input("Enter patient age: "),
        input("Enter diagnosis: "),
    )


def get_medical_record():
    print("\n--- Get Medical Record ---")
    handle_soap_request(soap_client.service.get_record, int(input("Enter medical record ID: ")))


def update_medical_record():
    print("\n--- Update Medical Record ---")
    handle_soap_request(
        soap_client.service.update_record,
        int(input("Enter medical record ID: ")),
        input("Enter new diagnosis: "),
    )


# --- DOCTORS FUNCTIONS (SOAP) ---
def add_doctor():
    print("\n--- Add Doctor ---")
    name = input("Enter doctor's name: ")
    specialty = input("Enter specialization: ")

    try:
        # SOAP call to add a doctor
        result = soap_client.service.add_doctor(name, specialty)
        print(f"Response: {result}")
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()

def list_doctors():
    print("\n--- List Doctors ---")
    try:
        # SOAP call to list doctors
        result = soap_client.service.list_doctors()
        print("\nDoctors:")
        for doctor in result:
            print(doctor)
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()

def update_doctor():
    print("\n--- Update Doctor ---")
    doctor_id = input("Enter doctor ID: ")
    new_specialty = input("Enter new specialization: ")

    try:
        # SOAP call to update a doctor's specialty
        result = soap_client.service.update_doctor(int(doctor_id), new_specialty)
        print(f"Response: {result}")
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()

def delete_doctor():
    print("\n--- Delete Doctor ---")
    doctor_id = input("Enter doctor ID: ")

    try:
        # SOAP call to delete a doctor by ID
        result = soap_client.service.delete_doctor(int(doctor_id))
        print(f"Response: {result}")
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()

# --- DOCTORS MENU ---
def doctors_menu():
    while True:
        clear_screen()
        print("\n--- Doctors Menu ---")
        print("1. Add Doctor")
        print("2. List Doctors")
        print("3. Update Doctor")
        print("4. Delete Doctor")
        print("q. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_doctor()
        elif choice == "2":
            list_doctors()
        elif choice == "3":
            update_doctor()
        elif choice == "4":
            delete_doctor()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")

def create_prescription():
    print("\n--- Create Prescription ---")
    try:
        patient_id = int(input("Enter patient ID: "))  # Change to patient ID
        prescription_details = input("Enter prescription details (medication): ")  # Use medication instead of medication, dosage, and instructions.

        # SOAP call to create a prescription
        result = soap_client.service.add_prescription(patient_id, prescription_details)
        print(f"Response: {result}")
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()


def list_prescriptions():
    print("\n--- List Prescriptions ---")
    patient_id = int(input("Enter patient ID: "))  # Prompt for patient ID to get prescriptions.
    try:
        # SOAP call to list prescriptions for a given patient ID
        prescriptions = soap_client.service.get_prescriptions(patient_id)
        print("\nPrescriptions:")
        for prescription in prescriptions:
            print(prescription)
    except Exception as e:
        print(f"SOAP Error: {e}")
    pause()


def prescriptions_menu():
    while True:
        clear_screen()
        print("\n--- Prescriptions Menu ---")
        print("1. Create Prescription")
        print("2. List Prescriptions")
        print("q. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_prescription()
        elif choice == "2":
            list_prescriptions()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")


# --- MENUS ---
def appointments_menu():
    while True:
        clear_screen()
        print("\n--- Appointments Menu ---")
        print("1. Create Appointment")
        print("2. List Appointments")
        print("3. Delete Appointment")
        print("q. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_appointment()
        elif choice == "2":
            list_appointments()
        elif choice == "3":
            delete_appointment()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")


def medical_records_menu():
    while True:
        clear_screen()
        print("\n--- Medical Records Menu ---")
        print("1. Create Medical Record")
        print("2. Get Medical Record")
        print("3. Update Medical Record")
        print("q. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_medical_record()
        elif choice == "2":
            get_medical_record()
        elif choice == "3":
            update_medical_record()
        elif choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    while True:
        clear_screen()
        print("\n=== Clinic Management System ===")
        print("1. Manage Appointments ")
        print("2. Manage Medical Records ")
        print("3. Manage Doctors ")
        print("4. Manage Prescriptions ")
        print("q. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            appointments_menu()
        elif choice == "2":
            medical_records_menu()
        elif choice == "3":
            doctors_menu()
        elif choice == "4":
            prescriptions_menu()
        elif choice == "q":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# --- Run the program ---
if __name__ == "__main__":
    main_menu()

