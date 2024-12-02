from spyne import rpc, ServiceBase, Integer, String, Fault
from database.models import MedicalRecord, session

class MedicalRecordsService(ServiceBase):
    @rpc(String, String, String, _returns=String)
    def create_record(ctx, name, age, diagnosis):
        """Create a new medical record."""
        record = MedicalRecord(patient_name=name, details=f"Age: {age}, Diagnosis: {diagnosis}")
        session.add(record)
        session.commit()
        return f"Dossier médical pour {name} créé avec succès, ID: {record.id}"

    @rpc(Integer, _returns=String)
    def get_record(ctx, patient_id):
        """Retrieve a medical record by ID."""
        record = session.query(MedicalRecord).filter_by(id=patient_id).first()
        if not record:
            raise Fault(faultcode="Client", faultstring="Erreur : Aucun dossier trouvé pour cet ID.")
        return f"Nom: {record.patient_name}, Détails: {record.details}"

    @rpc(Integer, String, _returns=String)
    def update_record(ctx, patient_id, new_diagnosis):
        """Update an existing medical record."""
        record = session.query(MedicalRecord).filter_by(id=patient_id).first()
        if not record:
            raise Fault(faultcode="Client", faultstring="Erreur : Aucun dossier trouvé pour cet ID.")
        record.details = new_diagnosis
        session.commit()
        return f"Diagnostic mis à jour pour l'ID {patient_id}: {new_diagnosis}"

    @rpc(Integer, _returns=String)
    def delete_record(ctx, patient_id):
        """Delete a medical record by ID."""
        record = session.query(MedicalRecord).filter_by(id=patient_id).first()
        if not record:
            raise Fault(faultcode="Client", faultstring="Erreur : Aucun dossier trouvé pour cet ID.")
        session.delete(record)
        session.commit()
        return f"Dossier ID {patient_id} supprimé avec succès."
