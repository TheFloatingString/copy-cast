"""
Tried using Flask... issues with websockets...
Will try Fast API instead.
"""

import socketserver
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/test")
def home():
    return "Welcome to repli.cate's Rest API!", 200

@socketio.on("test_socket", namespace="/test_socket")
def test_socket(data):
    print(f"from client: {data}")
    emit("response", {"from": "server"})

if __name__ == "__main__":
    # app.run(port=8080, debug=True)
    socketio.run(app, host="127.0.0.1", port=8080, debug=True)
