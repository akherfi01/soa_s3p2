from flask import Blueprint, jsonify, request
from database.models import Appointment, session
from notifications import send_email_notification

appointments_bp = Blueprint("appointments", __name__)

# Create an appointment
@appointments_bp.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()
    appointment = Appointment(
        patient_name=data["patient_name"],
        email=data["email"],  # Include email in the request
        date=data["date"],
        time=data["time"],
        reason=data["reason"]
    )
    session.add(appointment)
    session.commit()

    # Notify via email
    subject = "Appointment Confirmation"
    message = f"""
    Dear {appointment.patient_name},

    Your appointment has been confirmed:
    - Date: {appointment.date}
    - Time: {appointment.time}
    - Reason: {appointment.reason}

    Thank you for choosing our clinic.
    """
    send_email_notification(appointment.email, subject, message)

    return jsonify({"message": "Rendez-vous créé avec succès", "id": appointment.id}), 201

# Get all appointments
@appointments_bp.route("/appointments", methods=["GET"])
def get_appointments():
    appointments = session.query(Appointment).all()
    if not appointments:
        return jsonify({"message": "Aucun rendez-vous trouvé"}), 404
    return jsonify([{
        "id": appointment.id,
        "patient_name": appointment.patient_name,
        "email": appointment.email,
        "date": appointment.date,
        "time": appointment.time,
        "reason": appointment.reason
    } for appointment in appointments])

# Delete an appointment
@appointments_bp.route("/appointments/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if not appointment:
        return jsonify({"error": "Rendez-vous non trouvé"}), 404

    # Notify via email
    subject = "Appointment Cancellation"
    message = f"""
    Dear {appointment.patient_name},

    Your appointment scheduled on {appointment.date} at {appointment.time} has been canceled.

    We hope to assist you again in the future.

    Regards,
    Clinic
    """
    send_email_notification(appointment.email, subject, message)

    session.delete(appointment)
    session.commit()
    return jsonify({"message": "Rendez-vous annulé avec succès"})
