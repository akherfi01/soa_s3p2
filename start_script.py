import threading
import time
from subprocess import Popen

# Function to start the server
def start_server():
    # Example: Running the Flask server (replace with your actual command)
    print("Starting server...")
    Popen(["python", "/app/soa_s3p2/project/app.py"])  # Start the server

# Function to start the client
def start_client():
    # Example: Running the client script (replace with your actual command)
    print("Starting client...")
    Popen(["python", "/app/soa_s3p2/project/p.py"])  # Start the client

# Function to start both server and client in separate threads
def start():
    # Create thread for server
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Give the server a short time to initialize
    time.sleep(2)  # Adjust time if necessary for your server to start

    # Create thread for client
    client_thread = threading.Thread(target=start_client)
    client_thread.start()

    # Optionally, wait for both threads to finish
    server_thread.join()
    client_thread.join()

if __name__ == "__main__":
    start()

