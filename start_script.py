import threading
import time
import subprocess

# Function to start the server in the background
def start_server():
    print("Starting server in the background...")
    with open("/dev/null", "wb") as devnull:
        subprocess.Popen(
            ["python", "/app/soa_s3p2/project/app.py"],
            stdout=devnull,
            stderr=devnull,
        )

# Function to start the client in the foreground
def start_client():
    print("Starting client in the foreground...")
    subprocess.run(["python", "/app/soa_s3p2/project/p.py"])

# Function to start both server and client
def start():
    # Create a thread for the server
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Give the server some time to initialize
    time.sleep(2)  # Adjust this delay as needed

    # Start the client in the foreground
    start_client()

if __name__ == "__main__":
    start()

