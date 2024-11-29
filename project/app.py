from flask import Flask, request
from zeep import Client
app = Flask(__name__)

@app.route('/soap/medicalrecords', methods=['POST'])
def medical_record_service():
    # Load and execute WSDL-based service
    wsdl_path = './medical_records/wsdl/medical_record_service.wsdl'
    client = Client(wsdl_path)
    # Parse request and call appropriate methods
    return "SOAP Service for Medical Records"

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/soap/prescriptions', methods=['POST'])
def prescription_service():
    wsdl_path = './prescriptions/wsdl/prescription_service.wsdl'
    client = Client(wsdl_path)
    return "SOAP Service for Prescriptions"
@app.route('/soap/doctors', methods=['POST'])
def doctor_service():
    wsdl_path = './doctors/wsdl/doctor_service.wsdl'
    client = Client(wsdl_path)
    return "SOAP Service for Doctors"
