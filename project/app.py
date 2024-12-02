from flask import Flask
from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Import SOAP Services
from medical_records.medical_record_service import MedicalRecordsService
from prescriptions.prescription_service import PrescriptionsService
from doctors.doctor_service import DoctorsService

# Import REST Services
from rest_services.appointments import appointments_bp
from rest_services.notifications import notifications_bp, configure_mail
from rest_services.follow_up import follow_up_bp

# Create Flask App
app = Flask(__name__)

# Configure Mail for Notifications
configure_mail(app)

# Register REST Blueprints
app.register_blueprint(appointments_bp, url_prefix='/api')
app.register_blueprint(notifications_bp, url_prefix='/api')
app.register_blueprint(follow_up_bp, url_prefix='/api')

# Create SOAP Application
soap_app = Application(
    [MedicalRecordsService, PrescriptionsService, DoctorsService],
    tns="clinic.services",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# Add SOAP Dispatcher Middleware
app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app, {"/soap": WsgiApplication(soap_app)}
)

@app.route("/")
def home():
    return "Services disponibles:\nSOAP: /soap\nREST: /api"

if __name__ == "__main__":
    print("Running application...")
    print("SOAP Services available at /soap")
    print("REST Services available at /api")
    app.run(host="0.0.0.0", port=5000, debug=True)
