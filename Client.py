import socket
import time


def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for _ in range(5):
            try:
                s.sendall(b"ping")
                print("Sent: ping")
                data = s.recv(1024)
                if not data:
                    break
                if data.decode() == "pong":
                    print(f"Received: {data.decode()}")
                else:
                    print(f"Received unknown message: {data.decode()}")
            except Exception as e:
                print(f"Error: {e}")
                break
            time.sleep(1)


if __name__ == "__main__":
    start_client('127.0.0.1', 65432)