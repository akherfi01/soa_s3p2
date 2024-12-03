from flask import Blueprint, jsonify
from database.models import PatientHistory, session

patient_tracking_bp = Blueprint("patient_tracking", __name__)

# Get consultation history for a patient
@patient_tracking_bp.route("/patients/<int:patient_id>/history", methods=["GET"])
def get_patient_history(patient_id):
    history = session.query(PatientHistory).filter_by(patient_id=patient_id).all()
    if not history:
        return jsonify({"error": "Aucun historique trouvé pour ce patient"}), 404
    return jsonify([{
        "id": record.id,
        "date": record.date,
        "doctor": record.doctor,
        "report": record.report
    } for record in history])
