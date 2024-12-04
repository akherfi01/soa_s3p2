import os
import requests
from time import sleep

# Define API endpoints for REST services
REST_API_BASE = "http://localhost:5000/api"
SOFT_API_BASE = "http://localhost:5000/soap"

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def menu(title, options):
    """Display a menu and get the user's choice."""
    clear_screen()
    print(f"--- {title} ---\n")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("q. Quit\n0. Exit")
    return input("Please select an option: ")

def main():
    """Main menu loop to interact with SOAP and REST services."""
    while True:
        choice = menu("Main Menu", [
            "Medical Records",
            "Doctors",
            "Prescriptions",
            "Appointments",
            "Patient Tracking",
            "Email Notifications"
        ])

        if choice == 'q' or choice == '0':
            break

        elif choice == '1':  # Medical Records SOAP
            while True:
                sub_choice = menu("Medical Records", [
                    "Create a Record",
                    "Get a Record",
                    "Update a Record",
                    "Delete a Record"
                ])
                if sub_choice == 'q' or sub_choice == '0':
                    break
                elif sub_choice == '1':  # Create Record
                    name = input("Enter patient name: ")
                    age = input("Enter age: ")
                    diagnosis = input("Enter diagnosis: ")
                    # SOAP request to create record
                    response = requests.post(f"{SOFT_API_BASE}/create_record", data={"name": name, "age": age, "diagnosis": diagnosis})
                    print(response.text)

                elif sub_choice == '2':  # Get Record
                    patient_id = input("Enter patient ID: ")
                    # SOAP request to get record
                    response = requests.get(f"{SOFT_API_BASE}/get_record/{patient_id}")
                    print(response.text)

                elif sub_choice == '3':  # Update Record
                    patient_id = input("Enter patient ID: ")
                    new_diagnosis = input("Enter new diagnosis: ")
                    # SOAP request to update record
                    response = requests.put(f"{SOFT_API_BASE}/update_record/{patient_id}", data={"new_diagnosis": new_diagnosis})
                    print(response.text)

                elif sub_choice == '4':  # Delete Record
                    patient_id = input("Enter patient ID: ")
                    # SOAP request to delete record
                    response = requests.delete(f"{SOFT_API_BASE}/delete_record/{patient_id}")
                    print(response.text)

        elif choice == '2':  # Doctors SOAP
            while True:
                sub_choice = menu("Doctors", [
                    "Add a Doctor",
                    "Get a Doctor",
                    "Update a Doctor",
                    "Delete a Doctor",
                    "List all Doctors"
                ])
                if sub_choice == 'q' or sub_choice == '0':
                    break
                elif sub_choice == '1':  # Add Doctor
                    name = input("Enter doctor name: ")
                    specialty = input("Enter doctor specialty: ")
                    # SOAP request to add doctor
                    response = requests.post(f"{SOFT_API_BASE}/add_doctor", data={"name": name, "specialty": specialty})
                    print(response.text)

                elif sub_choice == '2':  # Get Doctor
                    doctor_id = input("Enter doctor ID: ")
                    # SOAP request to get doctor
                    response = requests.get(f"{SOFT_API_BASE}/get_doctor/{doctor_id}")
                    print(response.text)

                elif sub_choice == '3':  # Update Doctor
                    doctor_id = input("Enter doctor ID: ")
                    new_specialty = input("Enter new specialty: ")
                    # SOAP request to update doctor
                    response = requests.put(f"{SOFT_API_BASE}/update_doctor/{doctor_id}", data={"new_specialty": new_specialty})
                    print(response.text)

                elif sub_choice == '4':  # Delete Doctor
                    doctor_id = input("Enter doctor ID: ")
                    # SOAP request to delete doctor
                    response = requests.delete(f"{SOFT_API_BASE}/delete_doctor/{doctor_id}")
                    print(response.text)

                elif sub_choice == '5':  # List all Doctors
                    response = requests.get(f"{SOFT_API_BASE}/list_doctors")
                    print(response.text)

        elif choice == '3':  # Prescriptions SOAP
            while True:
                sub_choice = menu("Prescriptions", [
                    "Add a Prescription",
                    "Get Prescriptions"
                ])
                if sub_choice == 'q' or sub_choice == '0':
                    break
                elif sub_choice == '1':  # Add Prescription
                    patient_id = input("Enter patient ID: ")
                    prescription_details = input("Enter prescription details: ")
                    # SOAP request to add prescription
                    response = requests.post(f"{SOFT_API_BASE}/add_prescription", data={"patient_id": patient_id, "prescription_details": prescription_details})
                    print(response.text)

                elif sub_choice == '2':  # Get Prescriptions
                    patient_id = input("Enter patient ID: ")
                    # SOAP request to get prescriptions
                    response = requests.get(f"{SOFT_API_BASE}/get_prescriptions/{patient_id}")
                    print(response.text)

        elif choice == '4':  # Appointments REST
            while True:
                sub_choice = menu("Appointments", [
                    "Create an Appointment",
                    "Get All Appointments",
                    "Delete an Appointment"
                ])
                if sub_choice == 'q' or sub_choice == '0':
                    break
                elif sub_choice == '1':  # Create Appointment
                    patient_name = input("Enter patient name: ")
                    email = input("Enter email: ")
                    date = input("Enter date (YYYY-MM-DD): ")
                    time = input("Enter time (HH:MM): ")
                    reason = input("Enter reason: ")
                    response = requests.post(f"{REST_API_BASE}/appointments", json={
                        "patient_name": patient_name, "email": email, "date": date, "time": time, "reason": reason
                    })
                    print(response.json())

                elif sub_choice == '2':  # Get All Appointments
                    response = requests.get(f"{REST_API_BASE}/appointments")
                    print(response.json())

                elif sub_choice == '3':  # Delete Appointment
                    appointment_id = input("Enter appointment ID: ")
                    response = requests.delete(f"{REST_API_BASE}/appointments/{appointment_id}")
                    print(response.json())

        elif choice == '5':  # Patient Tracking REST
            while True:
                sub_choice = menu("Patient Tracking", [
                    "Get Patient History"
                ])
                if sub_choice == 'q' or sub_choice == '0':
                    break
                elif sub_choice == '1':  # Get Patient History
                    patient_id = input("Enter patient ID: ")
                    response = requests.get(f"{REST_API_BASE}/patients/{patient_id}/history")
                    print(response.json())

        elif choice == '6':  # Email Notifications REST
            while True:
                sub_choice = menu("Email Notifications", [
                    "Send an Email Notification"
                ])
                if sub_choice == 'q' or sub_choice == '0':
                    break
                elif sub_choice == '1':  # Send Email
                    recipient = input("Enter recipient email: ")
                    subject = input("Enter subject: ")
                    message = input("Enter message: ")
                    response = requests.post(f"{REST_API_BASE}/notifications", json={
                        "recipient": recipient, "subject": subject, "message": message
                    })
                    print(response.json())

if __name__ == "__main__":
    main()

