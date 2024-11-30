doctors_db = {}
# Service de gestion des docteurs

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
