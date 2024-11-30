prescriptions_db = {}
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