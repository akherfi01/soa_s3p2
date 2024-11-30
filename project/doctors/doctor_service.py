from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable, Fault
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from database.models import Doctor, session

class DoctorService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Integer)
    def add_doctor(ctx, name, specialty):
        """Add a new doctor."""
        doctor = Doctor(name=name, specialty=specialty)
        session.add(doctor)
        session.commit()
        return doctor.id

    @rpc(Integer, _returns=Unicode)
    def read_doctor(ctx, doctor_id):
        """Read doctor details by ID."""
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if not doctor:
            raise Fault(faultcode="Client", faultstring="Doctor not found")
        return f"Name: {doctor.name}, Specialty: {doctor.specialty}"

    @rpc(Integer, Unicode, Unicode, _returns=Unicode)
    def update_doctor(ctx, doctor_id, name, specialty):
        """Update an existing doctor."""
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if not doctor:
            raise Fault(faultcode="Client", faultstring="Doctor not found")
        doctor.name = name
        doctor.specialty = specialty
        session.commit()
        return "Doctor updated successfully"

    @rpc(Integer, _returns=Unicode)
    def delete_doctor(ctx, doctor_id):
        """Delete a doctor by ID."""
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if not doctor:
            raise Fault(faultcode="Client", faultstring="Doctor not found")
        session.delete(doctor)
        session.commit()
        return "Doctor deleted successfully"

app = Application(
    [DoctorService],
    tns="http://example.com/doctors",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(app)
