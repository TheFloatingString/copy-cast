import socket

def test_server():

    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    conn, address = server_socket.accept()

    print(f"new connection: {address}")

    while True:

        data = conn.recv(1024).decode()

        if not data:
            break
    
        print(f"client msg {data}")
        conn.send("server says hi!".encode())

    conn.close()

if __name__ == "__main__":
    test_server()

