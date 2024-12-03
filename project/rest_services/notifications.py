from flask import Blueprint, jsonify, request

notifications_bp = Blueprint("notifications", __name__)

# Envoi des notifications
@notifications_bp.route("/notifications", methods=["POST"])
def send_notification():
    data = request.get_json()
    recipient = data["recipient"]
    notification_type = data["type"]  # "email" ou "sms"
    message = data["message"]

    # Simuler l'envoi de la notification
    if notification_type == "email":
        return jsonify({"message": f"E-mail envoyé à {recipient}", "content": message}), 200
    elif notification_type == "sms":
        return jsonify({"message": f"SMS envoyé à {recipient}", "content": message}), 200
    else:
        return jsonify({"error": "Type de notification non supporté"}), 400
