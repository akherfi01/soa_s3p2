from flask import Blueprint, request, jsonify
from database.models import Base, session, create_engine
from sqlalchemy import Column, Integer, String, DateTime

# Define Appointment Model
class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, nullable=False)
    doctor_id = Column(Integer, nullable=False)
    appointment_time = Column(DateTime, nullable=False)
    status = Column(String, default="booked")  # booked, canceled

Base.metadata.create_all(bind=create_engine('sqlite:///clinic.db'))

# Create Blueprint
appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    appointment = Appointment(
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id'],
        appointment_time=data['appointment_time']
    )
    session.add(appointment)
    session.commit()
    return jsonify({"message": "Appointment created", "appointment_id": appointment.id}), 201

@appointments_bp.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify({
        "id": appointment.id,
        "patient_id": appointment.patient_id,
        "doctor_id": appointment.doctor_id,
        "appointment_time": appointment.appointment_time,
        "status": appointment.status
    })

@appointments_bp.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if not appointment:
        return jsonify({"error": "Appointment not found"}), 404
    appointment.status = "canceled"
    session.commit()
    return jsonify({"message": "Appointment canceled"})

