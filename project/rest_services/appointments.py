from flask import Blueprint, jsonify, request

appointments_bp = Blueprint("appointments", __name__)

# Base de données simulée
appointments_db = {}

# Prendre un rendez-vous
@appointments_bp.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.get_json()
    appointment_id = len(appointments_db) + 1
    appointments_db[appointment_id] = {
        "patient_name": data["patient_name"],
        "date": data["date"],
        "time": data["time"],
        "reason": data["reason"]
    }
    return jsonify({"message": "Rendez-vous créé avec succès", "id": appointment_id}), 201

# Consulter tous les rendez-vous
@appointments_bp.route("/appointments", methods=["GET"])
def get_appointments():
    return jsonify(appointments_db)

# Annuler un rendez-vous
@appointments_bp.route("/appointments/<int:appointment_id>", methods=["DELETE"])
def delete_appointment(appointment_id):
    if appointment_id in appointments_db:
        del appointments_db[appointment_id]
        return jsonify({"message": "Rendez-vous annulé avec succès"})
    return jsonify({"error": "Rendez-vous non trouvé"}), 404
