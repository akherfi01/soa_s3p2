from zeep import Client

# Replace with the actual WSDL URL or file path
wsdl = "http://localhost:5000/soap/?wsdl"  # For example, 'http://example.com/service?wsdl'
client = Client(wsdl=wsdl)

#print(dir(client.service))
#response = client.service.add_doctor(name="Dr. Smith", specialty="Cardiology")
#print(response)
rep = client.service.get_doctor(doctor_id=1)
print(rep)