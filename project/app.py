from flask import Flask, Response
from spyne.server.wsgi import WsgiApplication
from medical_records.medical_record_service import app as medical_record_app
from prescriptions.prescription_service import app as prescription_app
from doctors.doctor_service import app as doctor_app

app = Flask(__name__)

@app.route('/soap/medicalrecords', methods=['POST', 'GET'])
def medical_record_service():
    """SOAP Service for Medical Records"""
    wsgi_app = WsgiApplication(medical_record_app)
    return Response(wsgi_app, content_type="text/xml")

@app.route('/soap/prescriptions', methods=['POST', 'GET'])
def prescription_service():
    """SOAP Service for Prescriptions"""
    wsgi_app = WsgiApplication(prescription_app)
    return Response(wsgi_app, content_type="text/xml")

@app.route('/soap/doctors', methods=['POST', 'GET'])
def doctor_service():
    """SOAP Service for Doctors"""
    wsgi_app = WsgiApplication(doctor_app)
    return Response(wsgi_app, content_type="text/xml")

if __name__ == "__main__":
    print("SOAP Services running at:")
    print("  Medical Records: http://localhost:8000/soap/medicalrecords/?wsdl")
    print("  Prescriptions:   http://localhost:8000/soap/prescriptions/?wsdl")
    print("  Doctors:         http://localhost:8000/soap/doctors/?wsdl")
    app.run(port=8000, debug=True)
