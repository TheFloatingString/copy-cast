from http import client
import socket

def test_client():
    # host = socket.gethostname()
    host = "172.16.143.147"
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = "client says hi!"

    while True:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print(f"server message: {data}")

        message = "client says hi!"

    client_socket.close()

if __name__ == "__main__":
    test_client()