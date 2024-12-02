from spyne import rpc, ServiceBase, Integer, String, Iterable, Fault
from database.models import Prescription, session

class PrescriptionsService(ServiceBase):
    @rpc(Integer, String, _returns=String)
    def add_prescription(ctx, patient_id, prescription_details):
        """Add a prescription for a patient."""
        prescription = Prescription(patient_id=patient_id, medication=prescription_details
                                    )
        session.add(prescription)
        session.commit()
        return f"Prescription ajoutée pour le patient ID {patient_id}, ID de prescription: {prescription.id}"

    @rpc(Integer, _returns=Iterable(String))
    def get_prescriptions(ctx, patient_id):
        """Retrieve all prescriptions for a patient by ID."""
        prescriptions = session.query(Prescription).filter_by(patient_id=patient_id).all()
        if not prescriptions:
            return ["Erreur : Aucune prescription trouvée pour cet ID."]
        return [f"ID: {p.id}, Médicament: {p.medication}" for p in prescriptions]
