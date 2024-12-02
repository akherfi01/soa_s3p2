from flask import Blueprint, jsonify
from database.models import session, MedicalRecord

follow_up_bp = Blueprint('follow_up', __name__)

@follow_up_bp.route('/patients/<int:patient_id>/history', methods=['GET'])
def get_patient_history(patient_id):
    records = session.query(MedicalRecord).filter_by(id=patient_id).all()
    if not records:
        return jsonify({"error": "No history found for this patient"}), 404
    return jsonify([{"patient_name": record.patient_name, "details": record.details} for record in records])

@follow_up_bp.route('/patients/history', methods=['GET'])
def get_all_patient_histories():
    """Retrieve all patients' histories."""
    records = session.query(MedicalRecord).all()
    if not records:
        return jsonify({"message": "No patient histories found"}), 404
    return jsonify([{"patient_id": record.id, "details": record.details} for record in records])

