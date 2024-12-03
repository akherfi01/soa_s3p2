from flask import Blueprint, jsonify

patient_tracking_bp = Blueprint("patient_tracking", __name__)

# Base de données simulée pour le suivi des patients
patient_history_db = {
    1: [
        {"date": "2024-01-15", "doctor": "Dr. John", "report": "Routine check-up"},
        {"date": "2024-02-20", "doctor": "Dr. Jane", "report": "Follow-up on flu"}
    ],
    2: [
        {"date": "2024-03-10", "doctor": "Dr. Smith", "report": "Initial consultation"}
    ]
}

# Afficher l'historique des consultations d'un patient
@patient_tracking_bp.route("/patients/<int:patient_id>/history", methods=["GET"])
def get_patient_history(patient_id):
    history = patient_history_db.get(patient_id)
    if history:
        return jsonify(history)
    return jsonify({"error": "Aucun historique trouvé pour ce patient"}), 404
