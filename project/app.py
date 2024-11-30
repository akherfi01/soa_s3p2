from spyne import Application, rpc, ServiceBase, Integer, Unicode, String, Iterable, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware



from ./medical_records/medical_record_service.py import *


# Création de l'application principale
flask_app = Flask(__name__)

soap_app = Application(
    [MedicalRecordsService, PrescriptionsService, DoctorsService],
    tns="clinic.services",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(),
)

flask_app.wsgi_app = DispatcherMiddleware(
    flask_app.wsgi_app, {"/soap": WsgiApplication(soap_app)}
)


@flask_app.route("/")
def home():
    return "Services SOAP disponibles à l'URL /soap"

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)
