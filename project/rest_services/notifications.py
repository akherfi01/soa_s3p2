import smtplib
from flask import Blueprint, jsonify, request

notifications_bp = Blueprint("notifications", __name__)

# Clinic's email credentials
CLINIC_EMAIL = "clinique.ask@gmail.com"
CLINIC_PASSWORD = "cxvgqnvzzwgqaydc"

@notifications_bp.route("/notifications", methods=["POST"])
def send_notification():
    """Endpoint to send email notifications."""
    data = request.get_json()
    recipient = data.get("recipient")
    subject = data.get("subject", "Clinic Notification")
    message = data.get("message")

    if not recipient or not message:
        return jsonify({"error": "Recipient and message are required"}), 400

    # Send email notification
    if send_email_notification(recipient, subject, message):
        return jsonify({"message": f"E-mail envoyé à {recipient}", "content": message}), 200
    else:
        return jsonify({"error": "Échec de l'envoi de l'email"}), 500

def send_email_notification(recipient, subject, message):
    """Helper function to send an email."""
    try:
        text = f"Subject: {subject}\n\n{message}"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(CLINIC_EMAIL, CLINIC_PASSWORD)
        server.sendmail(CLINIC_EMAIL, recipient, text)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False
