from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import sqlite3

class CalculatorService(ServiceBase):
    @rpc(Integer, _returns=)
    def create_record(ctx, r_fname, r_lname):
        connection = sqlite3.connect("medical_records.db")
        r_cursor = connection.cursor()
        r_cursor.execute("""
            CREATE TABLE IF NOT EXISTS medical_records (
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            )
            """)
        r_cursor.execute("""
            INSERT INTO medical_records (first_name, last_name)
            VALUES (?, ?)
            """, (r_fname, r_lname))
        connection.commit()
        connection.close()

app = Application(
    [CalculatorService],
    tns="http://127.0.0.1/calculator",
    in_protocol=Soap11(),
    out_protocol=Soap11(),
)

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    server = make_server("127.0.0.1", 8000, WsgiApplication(app))
    print("SOAP service running at http://127.0.0.1:8000")
    server.serve_forever()
