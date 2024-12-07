from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# Import des services SOAP
from medical_records.medical_record_service import MedicalRecordsService
from prescriptions.prescription_service import PrescriptionsService
from doctors.doctor_service import DoctorsService

# Import des services REST
from rest_services.appointments import appointments_bp
from rest_services.notifications import notifications_bp
from rest_services.follow_up import patient_tracking_bp


# Créer l'application Flask
app = Flask(__name__)

# Enregistrer les services REST comme blueprints
app.register_blueprint(appointments_bp, url_prefix="/api")
app.register_blueprint(notifications_bp, url_prefix="/api")
app.register_blueprint(patient_tracking_bp, url_prefix="/api")

# Configuration des services SOAP avec Spyne
soap_app = Application(
    [MedicalRecordsService, PrescriptionsService, DoctorsService],
    tns="clinic.services",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

# Fusionner Flask et Spyne (SOAP)
app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app, {"/soap": WsgiApplication(soap_app)}
)

# Route principale
@app.route("/")
def home():
    return "Bienvenue sur l'application combinée REST et SOAP."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=54321)
