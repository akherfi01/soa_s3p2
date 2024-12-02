from spyne import rpc, ServiceBase, Integer, String, Iterable, Fault
from database.models import Doctor, session

class DoctorsService(ServiceBase):
    @rpc(String, String, _returns=String)
    def add_doctor(ctx, name, specialty):
        """Add a new doctor."""
        doctor = Doctor(name=name, specialty=specialty)
        session.add(doctor)
        session.commit()
        return f"Médecin {name} ajouté avec succès, ID: {doctor.id}"

    @rpc(Integer, _returns=String)
    def get_doctor(ctx, doctor_id):
        """Retrieve a doctor's details by ID."""
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if not doctor:
            raise Fault(faultcode="Client", faultstring="Erreur : Médecin introuvable.")
        return f"Nom: {doctor.name}, Spécialité: {doctor.specialty}"

    @rpc(Integer, String, _returns=String)
    def update_doctor(ctx, doctor_id, new_specialty):
        """Update a doctor's specialty."""
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if not doctor:
            raise Fault(faultcode="Client", faultstring="Erreur : Médecin introuvable.")
        doctor.specialty = new_specialty
        session.commit()
        return f"Spécialité mise à jour pour l'ID {doctor_id}: {new_specialty}"

    @rpc(Integer, _returns=String)
    def delete_doctor(ctx, doctor_id):
        """Delete a doctor by ID."""
        doctor = session.query(Doctor).filter_by(id=doctor_id).first()
        if not doctor:
            raise Fault(faultcode="Client", faultstring="Erreur : Médecin introuvable.")
        session.delete(doctor)
        session.commit()
        return f"Médecin ID {doctor_id} supprimé avec succès."

    @rpc(_returns=Iterable(String))
    def list_doctors(ctx):
        """List all doctors."""
        doctors = session.query(Doctor).all()
        return [f"ID: {d.id}, Nom: {d.name}, Spécialité: {d.specialty}" for d in doctors]
