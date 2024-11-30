from spyne import rpc, ServiceBase, Integer, String
patients_db = {}


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

