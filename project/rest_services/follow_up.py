from flask import Blueprint, jsonify
from database.models import MedicalRecord, session

patient_tracking_bp = Blueprint("patient_tracking", __name__)

# Get consultation history for a patient
@patient_tracking_bp.route("/patients/<int:patient_id>/history", methods=["GET"])
def get_patient_history(patient_id):
    # Query medical records based on patient_id
    history = session.query(MedicalRecord).filter_by(id=patient_id).all()
    
    if not history:
        return jsonify({"error": "Aucun historique trouvé pour ce patient"}), 404
    
    return jsonify([{
        "id": record.id,
        "patient_name": record.patient_name,
        "details": record.details
    } for record in history])
