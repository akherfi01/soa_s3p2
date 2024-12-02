from flask import Blueprint, request, jsonify
from flask_mail import Mail, Message

# Setup Mail
mail = Mail()
notifications_bp = Blueprint('notifications', __name__)

def configure_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.example.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'your-email@example.com'
    app.config['MAIL_PASSWORD'] = 'your-password'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    mail.init_app(app)

@notifications_bp.route('/notifications/email', methods=['POST'])
def send_email_notification():
    data = request.json
    msg = Message(data['subject'], sender='your-email@example.com', recipients=[data['recipient']])
    msg.body = data['message']
    mail.send(msg)
    return jsonify({"message": "Email sent"}), 200
