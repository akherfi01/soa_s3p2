from spyne import Application, rpc, ServiceBase, Integer, Unicode, Fault
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from database.models import MedicalRecord, session

class MedicalRecordService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Integer)
    def create_record(ctx, patient_name, details):
        """Create a new medical record."""
        record = MedicalRecord(patient_name=patient_name, details=details)
        session.add(record)
        session.commit()
        return record.id

    @rpc(Integer, _returns=Unicode)
    def read_record(ctx, record_id):
        """Read a medical record by ID."""
        record = session.query(MedicalRecord).filter_by(id=record_id).first()
        if not record:
            raise Fault(faultcode="Client", faultstring="Medical record not found")
        return f"Patient Name: {record.patient_name}, Details: {record.details}"

    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def update_record(ctx, record_id, patient_name, details):
        """Update an existing medical record."""
        record = session.query(MedicalRecord).filter_by(id=record_id).first()
        if not record:
            raise Fault(faultcode="Client", faultstring="Medical record not found")
        record.patient_name = patient_name
        record.details = details
        session.commit()
        return "Medical record updated successfully"

    @rpc(Integer, _returns=Unicode)
    def delete_record(ctx, record_id):
        """Delete a medical record by ID."""
        record = session.query(MedicalRecord).filter_by(id=record_id).first()
        if not record:
            raise Fault(faultcode="Client", faultstring="Medical record not found")
        session.delete(record)
        session.commit()
        return "Medical record deleted successfully"

# Spyne Application
app = Application(
    [MedicalRecordService],
    tns="http://example.com/medicalrecords",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(app)
