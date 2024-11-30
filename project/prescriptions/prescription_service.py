from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, Fault
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from database.models import Prescription, session

class PrescriptionService(ServiceBase):
    @rpc(Integer, Unicode, Unicode, _returns=Integer)
    def add_prescription(ctx, patient_id, medication, dosage):
        """Add a new prescription for a patient."""
        prescription = Prescription(patient_id=patient_id, medication=medication, dosage=dosage)
        session.add(prescription)
        session.commit()
        return prescription.id

    @rpc(Integer, _returns=Unicode)
    def read_prescription(ctx, prescription_id):
        """Read prescription details by ID."""
        prescription = session.query(Prescription).filter_by(id=prescription_id).first()
        if not prescription:
            raise Fault(faultcode="Client", faultstring="Prescription not found")
        return f"Patient ID: {prescription.patient_id}, Medication: {prescription.medication}, Dosage: {prescription.dosage}"

    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def update_prescription(ctx, prescription_id, medication, dosage):
        """Update an existing prescription."""
        prescription = session.query(Prescription).filter_by(id=prescription_id).first()
        if not prescription:
            raise Fault(faultcode="Client", faultstring="Prescription not found")
        prescription.medication = medication
        prescription.dosage = dosage
        session.commit()
        return "Prescription updated successfully"

    @rpc(Integer, _returns=Unicode)
    def delete_prescription(ctx, prescription_id):
        """Delete a prescription by ID."""
        prescription = session.query(Prescription).filter_by(id=prescription_id).first()
        if not prescription:
            raise Fault(faultcode="Client", faultstring="Prescription not found")
        session.delete(prescription)
        session.commit()
        return "Prescription deleted successfully"

app = Application(
    [PrescriptionService],
    tns="http://example.com/prescriptions",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(app)
