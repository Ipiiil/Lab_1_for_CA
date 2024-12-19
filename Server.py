import socket


def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    if data.decode() == "ping":
                        conn.sendall(b"pong")
                        print("Sent: pong")
                    else:
                        print("Received unknown message, ignoring.")
                except Exception as e:
                    print(f"Error: {e}")
                    break


if __name__ == "__main__":
    start_server('127.0.0.1', 65432)