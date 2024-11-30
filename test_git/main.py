from spyne import Application, rpc, ServiceBase, Integer, Unicode, String, Iterable, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# Simulations de bases de données
patients_db = {}
prescriptions_db = {}
doctors_db = {}

# Service de gestion des dossiers médicaux
class MedicalRecordsService(ServiceBase):
    @rpc(Integer, String, String, String, _returns=String)
    def create_record(ctx, patient_id, name, age, diagnosis):
        if patient_id in patients_db:
            return "Erreur : Le dossier du patient existe déjà."
        patients_db[patient_id] = {"name": name, "age": age, "diagnosis": diagnosis}
        return f"Dossier médical du patient {name} créé avec succès."

    @rpc(Integer, _returns=String)
    def get_record(ctx, patient_id):
        record = patients_db.get(patient_id)
        if record:
            return f"Dossier : {record}"
        return "Erreur : Aucun dossier trouvé pour cet ID."

    @rpc(Integer, String, _returns=String)
    def update_record(ctx, patient_id, new_diagnosis):
        if patient_id in patients_db:
            patients_db[patient_id]["diagnosis"] = new_diagnosis
            return f"Diagnostic mis à jour : {new_diagnosis}"
        return "Erreur : Aucun dossier trouvé pour cet ID."

    @rpc(Integer, _returns=String)
    def delete_record(ctx, patient_id):
        if patient_id in patients_db:
            del patients_db[patient_id]
            return "Dossier supprimé avec succès."
        return "Erreur : Aucun dossier trouvé pour cet ID."

# Service de gestion des prescriptions
class PrescriptionsService(ServiceBase):
    @rpc(Integer, String, _returns=String)
    def add_prescription(ctx, patient_id, prescription):
        if patient_id not in patients_db:
            return "Erreur : Aucun dossier médical pour cet ID."
        if patient_id not in prescriptions_db:
            prescriptions_db[patient_id] = []
        prescriptions_db[patient_id].append(prescription)
        return f"Prescription ajoutée pour le patient ID {patient_id}."

    @rpc(Integer, _returns=Iterable(String))
    def get_prescriptions(ctx, patient_id):
        if patient_id in prescriptions_db:
            return prescriptions_db[patient_id]
        return ["Erreur : Aucune prescription trouvée pour cet ID."]

# Service de gestion des médecins
class DoctorsService(ServiceBase):
    @rpc(Integer, String, String, _returns=String)
    def add_doctor(ctx, doctor_id, name, specialty):
        if doctor_id in doctors_db:
            return "Erreur : Le médecin existe déjà."
        doctors_db[doctor_id] = {"name": name, "specialty": specialty}
        return f"Médecin {name} ajouté avec succès."

    @rpc(Integer, String, _returns=String)
    def update_doctor(ctx, doctor_id, new_specialty):
        if doctor_id in doctors_db:
            doctors_db[doctor_id]["specialty"] = new_specialty
            return f"Spécialité mise à jour pour le médecin ID {doctor_id}."
        return "Erreur : Médecin introuvable."

    @rpc(Integer, _returns=String)
    def delete_doctor(ctx, doctor_id):
        if doctor_id in doctors_db:
            del doctors_db[doctor_id]
            return "Médecin supprimé avec succès."
        return "Erreur : Médecin introuvable."

    @rpc(_returns=Iterable(String))
    def list_doctors(ctx):
        return [f"ID: {id}, Nom: {info['name']}, Spécialité: {info['specialty']}" for id, info in doctors_db.items()]

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
